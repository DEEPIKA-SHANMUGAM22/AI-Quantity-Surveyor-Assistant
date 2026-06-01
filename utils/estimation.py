def estimate_materials(area):
    # More realistic assumptions (approx for residential building)

    cement_per_sqft = 0.12   # bags per sq.ft
    bricks_per_sqft = 7      # bricks per sq.ft
    steel_per_sqft = 2.5     # kg per sq.ft

    cement = area * cement_per_sqft
    bricks = area * bricks_per_sqft
    steel = area * steel_per_sqft

    return cement, bricks, steel

def estimate_cost(cement, bricks, steel, area):

    cement_cost = cement * 350
    brick_cost = bricks * 8
    steel_cost = steel * 70

    material_cost = cement_cost + brick_cost + steel_cost

    # Add missing components
    labour_cost = area * 300
    finishing_cost = area * 800

    total_cost = material_cost + labour_cost + finishing_cost

    return material_cost, labour_cost, finishing_cost, total_cost