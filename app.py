import streamlit as st
import cv2
import numpy as np

from utils.ml_model import train_model, predict_cost
from utils.image_processing import preprocess_image, detect_edges, detect_contours
from utils.estimation import estimate_materials, estimate_cost
from utils.report import generate_report

st.title("🏗 AI Quantity Surveyor Assistant")

uploaded_file = st.file_uploader("Upload Floor Plan", type=["png", "jpg", "jpeg"])

@st.cache_resource
def get_model():
    return train_model()

if uploaded_file:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, 1)

    st.image(img, caption="Uploaded Floor Plan", width=500)

    # Processing
    processed = preprocess_image(img)
    edges = detect_edges(processed)
    contours = detect_contours(processed)

    # 🔥 ADD HERE
    st.subheader("🧠 Computer Vision Output")

    col1, col2 = st.columns(2)

    with col1:
        st.write("Edges")
        st.image(edges, width=300)

    with col2:
        contour_img = img.copy()
        cv2.drawContours(contour_img, contours, -1, (0, 255, 0), 2)
        st.write("Detected Areas")
        st.image(contour_img, width=300)

    total_area = 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 1000:
            total_area += area

    st.write("📊 Pixel Area:", int(total_area))

    # Scale input
    real_width = st.number_input("Enter known dimension (ft)", value=70.0)

    pixel_width = img.shape[1]
    length_per_pixel = real_width / pixel_width
    scale = length_per_pixel ** 2

    real_area = total_area * scale

    st.subheader("📐 Area Estimation")
    st.write(f"Estimated Area: {round(real_area)} sq.ft")

    # Material estimation
    cement, bricks, steel = estimate_materials(real_area)

    st.subheader("🧱 Material Estimation")
    st.write(f"Cement: {round(cement)} bags")
    st.write(f"Bricks: {round(bricks)}")
    st.write(f"Steel: {round(steel)} kg")

    # Cost estimation
    material_cost, labour_cost, finishing_cost, total_cost = estimate_cost(
        cement, bricks, steel, real_area
    )

    cost_per_sqft = total_cost / real_area

    st.subheader("💰 Cost Estimation")
    st.write(f"Material Cost: ₹{round(material_cost)}")
    st.write(f"Labour Cost: ₹{round(labour_cost)}")
    st.write(f"Finishing Cost: ₹{round(finishing_cost)}")

    st.success(f"Total Cost: ₹{round(total_cost)}")
    st.write(f"Cost per sq.ft: ₹{round(cost_per_sqft)}")

    # 📄 PDF Report Button
if st.button("📄 Generate Report"):
    file_path = generate_report(real_area, cement, bricks, steel, total_cost)

    with open(file_path, "rb") as f:
        st.download_button(
            label="Download Report",
            data=f,
            file_name="QS_Report.pdf",
            mime="application/pdf"
        )

    # ML prediction
    model = get_model()
    ml_cost = predict_cost(model, real_area)

    st.subheader("🤖 ML Cost Prediction")
    st.write(f"Predicted Cost (ML): ₹{round(ml_cost)}")