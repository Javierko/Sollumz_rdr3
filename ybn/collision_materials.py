import bpy
from ..sollumz_properties import MaterialType
from collections import namedtuple

CollisionMaterial = namedtuple("CollisionMaterial", "name, ui_name, color")

collisionmats = [
    CollisionMaterial("DEFAULT", "Default", (255, 0, 255, 255)),
    CollisionMaterial("CONCRETE", "Concrete", (145, 145, 145, 255)),
    CollisionMaterial("CONCRETE_POTHOLE", "Concrete Pothole",
                      (145, 145, 145, 255)),
    CollisionMaterial("CONCRETE_DUSTY", "Concrete Dusty",
                      (145, 140, 130, 255)),
    CollisionMaterial("TARMAC", "Tarmac", (90, 90, 90, 255)),
    CollisionMaterial("TARMAC_PAINTED", "Tarmac Painted", (90, 90, 90, 255)),
    CollisionMaterial("TARMAC_POTHOLE", "Tarmac Pothole", (70, 70, 70, 255)),
    CollisionMaterial("RUMBLE_STRIP", "Rumble Strip", (90, 90, 90, 255)),
    CollisionMaterial("BREEZE_BLOCK", "Breeze Block", (145, 145, 145, 255)),
    CollisionMaterial("ROCK", "Rock", (185, 185, 185, 255)),
    CollisionMaterial("ROCK_MOSSY", "Rock Mossy", (185, 185, 185, 255)),
    CollisionMaterial("STONE", "Stone", (185, 185, 185, 255)),
    CollisionMaterial("COBBLESTONE", "Cobblestone", (185, 185, 185, 255)),
    CollisionMaterial("BRICK", "Brick", (195, 95, 30, 255)),
    CollisionMaterial("MARBLE", "Marble", (195, 155, 145, 255)),
    CollisionMaterial("PAVING_SLAB", "Paving Slab", (200, 165, 130, 255)),
    CollisionMaterial("SANDSTONE_SOLID", "Sandstone Solid",
                      (215, 195, 150, 255)),
    CollisionMaterial("SANDSTONE_BRITTLE",
                      "Sandstone Brittle", (205, 180, 120, 255)),
    CollisionMaterial("SAND_LOOSE", "Sand Loose", (235, 220, 190, 255)),
    CollisionMaterial("SAND_COMPACT", "Sand Compact", (250, 240, 220, 255)),
    CollisionMaterial("SAND_WET", "Sand Wet", (190, 185, 165, 255)),
    CollisionMaterial("SAND_TRACK", "Sand Track", (250, 240, 220, 255)),
    CollisionMaterial("SAND_UNDERWATER", "Sand Underwater",
                      (135, 130, 120, 255)),
    CollisionMaterial("SAND_DRY_DEEP", "Sand Dry Deep", (110, 100, 85, 255)),
    CollisionMaterial("SAND_WET_DEEP", "Sand Wet Deep", (110, 100, 85, 255)),
    CollisionMaterial("ICE", "Ice", (200, 250, 255, 255)),
    CollisionMaterial("ICE_TARMAC", "Ice Tarmac", (200, 250, 255, 255)),
    CollisionMaterial("SNOW_LOOSE", "Snow Loose", (255, 255, 255, 255)),
    CollisionMaterial("SNOW_COMPACT", "Snow Compact", (255, 255, 255, 255)),
    CollisionMaterial("SNOW_DEEP", "Snow Deep", (255, 255, 255, 255)),
    CollisionMaterial("SNOW_TARMAC", "Snow Tarmac", (255, 255, 255, 255)),
    CollisionMaterial("GRAVEL_SMALL", "Gravel Small", (255, 255, 255, 255)),
    CollisionMaterial("GRAVEL_LARGE", "Gravel Large", (255, 255, 255, 255)),
    CollisionMaterial("GRAVEL_DEEP", "Gravel Deep", (255, 255, 255, 255)),
    CollisionMaterial("GRAVEL_TRAIN_TRACK",
                      "Gravel Train Track", (145, 140, 130, 255)),
    CollisionMaterial("DIRT_TRACK", "Dirt Track", (175, 160, 140, 255)),
    CollisionMaterial("MUD_HARD", "Mud Hard", (175, 160, 140, 255)),
    CollisionMaterial("MUD_POTHOLE", "Mud Pothole", (105, 95, 75, 255)),
    CollisionMaterial("MUD_SOFT", "Mud Soft", (105, 95, 75, 255)),
    CollisionMaterial("MUD_UNDERWATER", "Mud Underwater", (75, 65, 50, 255)),
    CollisionMaterial("MUD_DEEP", "Mud Deep", (105, 95, 75, 255)),
    CollisionMaterial("MARSH", "Marsh", (105, 95, 75, 255)),
    CollisionMaterial("MARSH_DEEP", "Marsh Deep", (105, 95, 75, 255)),
    CollisionMaterial("SOIL", "Soil", (105, 95, 75, 255)),
    CollisionMaterial("CLAY_HARD", "Clay Hard", (160, 160, 160, 255)),
    CollisionMaterial("CLAY_SOFT", "Clay Soft", (160, 160, 160, 255)),
    CollisionMaterial("GRASS_LONG", "Grass Long", (130, 205, 75, 255)),
    CollisionMaterial("GRASS", "Grass", (130, 205, 75, 255)),
    CollisionMaterial("GRASS_SHORT", "Grass Short", (130, 205, 75, 255)),
    CollisionMaterial("HAY", "Hay", (240, 205, 125, 255)),
    CollisionMaterial("BUSHES", "Bushes", (85, 160, 30, 255)),
    CollisionMaterial("TWIGS", "Twigs", (115, 100, 70, 255)),
    CollisionMaterial("LEAVES", "Leaves", (70, 100, 50, 255)),
    CollisionMaterial("WOODCHIPS", "Woodchips", (115, 100, 70, 255)),
    CollisionMaterial("TREE_BARK", "Tree Bark", (115, 100, 70, 255)),
    CollisionMaterial("METAL_SOLID_SMALL",
                      "Metal Solid Small", (155, 180, 190, 255)),
    CollisionMaterial("METAL_SOLID_MEDIUM",
                      "Metal Solid Medium", (155, 180, 190, 255)),
    CollisionMaterial("METAL_SOLID_LARGE",
                      "Metal Solid Large", (155, 180, 190, 255)),
    CollisionMaterial("METAL_HOLLOW_SMALL",
                      "Metal Hollow Small", (155, 180, 190, 255)),
    CollisionMaterial("METAL_HOLLOW_MEDIUM",
                      "Metal Hollow Medium", (155, 180, 190, 255)),
    CollisionMaterial("METAL_HOLLOW_LARGE",
                      "Metal Hollow Large", (155, 180, 190, 255)),
    CollisionMaterial("METAL_CHAINLINK_SMALL",
                      "Metal Chainlink Small", (155, 180, 190, 255)),
    CollisionMaterial("METAL_CHAINLINK_LARGE",
                      "Metal Chainlink Large", (155, 180, 190, 255)),
    CollisionMaterial("METAL_CORRUGATED_IRON",
                      "Metal Corrugated Iron", (155, 180, 190, 255)),
    CollisionMaterial("METAL_GRILLE", "Metal Grille", (155, 180, 190, 255)),
    CollisionMaterial("METAL_RAILING", "Metal Railing", (155, 180, 190, 255)),
    CollisionMaterial("METAL_DUCT", "Metal Duct", (155, 180, 190, 255)),
    CollisionMaterial("METAL_GARAGE_DOOR",
                      "Metal Garage Door", (155, 180, 190, 255)),
    CollisionMaterial("METAL_MANHOLE", "Metal Manhole", (155, 180, 190, 255)),
    CollisionMaterial("WOOD_SOLID_SMALL", "Wood Solid Small",
                      (155, 130, 95, 255)),
    CollisionMaterial("WOOD_SOLID_MEDIUM",
                      "Wood Solid Medium", (155, 130, 95, 255)),
    CollisionMaterial("WOOD_SOLID_LARGE", "Wood Solid Large",
                      (155, 130, 95, 255)),
    CollisionMaterial("WOOD_SOLID_POLISHED",
                      "Wood Solid Polished", (155, 130, 95, 255)),
    CollisionMaterial("WOOD_FLOOR_DUSTY", "Wood Floor Dusty",
                      (165, 145, 110, 255)),
    CollisionMaterial("WOOD_HOLLOW_SMALL",
                      "Wood Hollow Small", (170, 150, 125, 255)),
    CollisionMaterial("WOOD_HOLLOW_MEDIUM",
                      "Wood Hollow Medium", (170, 150, 125, 255)),
    CollisionMaterial("WOOD_HOLLOW_LARGE",
                      "Wood Hollow Large", (170, 150, 125, 255)),
    CollisionMaterial("WOOD_CHIPBOARD", "Wood Chipboard",
                      (170, 150, 125, 255)),
    CollisionMaterial("WOOD_OLD_CREAKY", "Wood Old Creaky",
                      (155, 130, 95, 255)),
    CollisionMaterial("WOOD_HIGH_DENSITY",
                      "Wood High Density", (155, 130, 95, 255)),
    CollisionMaterial("WOOD_LATTICE", "Wood Lattice", (155, 130, 95, 255)),
    CollisionMaterial("CERAMIC", "Ceramic", (220, 210, 195, 255)),
    CollisionMaterial("ROOF_TILE", "Roof Tile", (220, 210, 195, 255)),
    CollisionMaterial("ROOF_FELT", "Roof Felt", (165, 145, 110, 255)),
    CollisionMaterial("FIBREGLASS", "Fibreglass", (255, 250, 210, 255)),
    CollisionMaterial("TARPAULIN", "Tarpaulin", (255, 250, 210, 255)),
    CollisionMaterial("PLASTIC", "Plastic", (255, 250, 210, 255)),
    CollisionMaterial("PLASTIC_HOLLOW", "Plastic Hollow",
                      (240, 230, 185, 255)),
    CollisionMaterial("PLASTIC_HIGH_DENSITY",
                      "Plastic High Density", (255, 250, 210, 255)),
    CollisionMaterial("PLASTIC_CLEAR", "Plastic Clear", (255, 250, 210, 255)),
    CollisionMaterial("PLASTIC_HOLLOW_CLEAR",
                      "Plastic Hollow Clear", (240, 230, 185, 255)),
    CollisionMaterial("PLASTIC_HIGH_DENSITY_CLEAR",
                      "Plastic High Density Clear", (255, 250, 210, 255)),
    CollisionMaterial("FIBREGLASS_HOLLOW",
                      "Fibreglass Hollow", (240, 230, 185, 255)),
    CollisionMaterial("RUBBER", "Rubber", (70, 70, 70, 255)),
    CollisionMaterial("RUBBER_HOLLOW", "Rubber Hollow", (70, 70, 70, 255)),
    CollisionMaterial("LINOLEUM", "Linoleum", (205, 150, 80, 255)),
    CollisionMaterial("LAMINATE", "Laminate", (170, 150, 125, 255)),
    CollisionMaterial("CARPET_SOLID", "Carpet Solid", (250, 100, 100, 255)),
    CollisionMaterial("CARPET_SOLID_DUSTY",
                      "Carpet Solid Dusty", (255, 135, 135, 255)),
    CollisionMaterial("CARPET_FLOORBOARD",
                      "Carpet Floorboard", (250, 100, 100, 255)),
    CollisionMaterial("CLOTH", "Cloth", (250, 100, 100, 255)),
    CollisionMaterial("PLASTER_SOLID", "Plaster Solid", (145, 145, 145, 255)),
    CollisionMaterial("PLASTER_BRITTLE", "Plaster Brittle",
                      (225, 225, 225, 255)),
    CollisionMaterial("CARDBOARD_SHEET", "Cardboard Sheet",
                      (120, 115, 95, 255)),
    CollisionMaterial("CARDBOARD_BOX", "Cardboard Box", (120, 115, 95, 255)),
    CollisionMaterial("PAPER", "Paper", (230, 225, 220, 255)),
    CollisionMaterial("FOAM", "Foam", (230, 235, 240, 255)),
    CollisionMaterial("FEATHER_PILLOW", "Feather Pillow",
                      (230, 230, 230, 255)),
    CollisionMaterial("POLYSTYRENE", "Polystyrene", (255, 250, 210, 255)),
    CollisionMaterial("LEATHER", "Leather", (250, 100, 100, 255)),
    CollisionMaterial("TVSCREEN", "Tvscreen", (115, 125, 125, 255)),
    CollisionMaterial("SLATTED_BLINDS", "Slatted Blinds",
                      (255, 250, 210, 255)),
    CollisionMaterial("GLASS_SHOOT_THROUGH",
                      "Glass Shoot Through", (205, 240, 255, 255)),
    CollisionMaterial("GLASS_BULLETPROOF",
                      "Glass Bulletproof", (115, 125, 125, 255)),
    CollisionMaterial("GLASS_OPAQUE", "Glass Opaque", (205, 240, 255, 255)),
    CollisionMaterial("PERSPEX", "Perspex", (205, 240, 255, 255)),
    CollisionMaterial("CAR_METAL", "Car Metal", (255, 255, 255, 255)),
    CollisionMaterial("CAR_PLASTIC", "Car Plastic", (255, 255, 255, 255)),
    CollisionMaterial("CAR_SOFTTOP", "Car Softtop", (250, 100, 100, 255)),
    CollisionMaterial("CAR_SOFTTOP_CLEAR",
                      "Car Softtop Clear", (250, 100, 100, 255)),
    CollisionMaterial("CAR_GLASS_WEAK", "Car Glass Weak",
                      (210, 245, 245, 255)),
    CollisionMaterial("CAR_GLASS_MEDIUM", "Car Glass Medium",
                      (210, 245, 245, 255)),
    CollisionMaterial("CAR_GLASS_STRONG", "Car Glass Strong",
                      (210, 245, 245, 255)),
    CollisionMaterial("CAR_GLASS_BULLETPROOF",
                      "Car Glass Bulletproof", (210, 245, 245, 255)),
    CollisionMaterial("CAR_GLASS_OPAQUE", "Car Glass Opaque",
                      (210, 245, 245, 255)),
    CollisionMaterial("WATER", "Water", (55, 145, 230, 255)),
    CollisionMaterial("BLOOD", "Blood", (205, 5, 5, 255)),
    CollisionMaterial("OIL", "Oil", (80, 65, 65, 255)),
    CollisionMaterial("PETROL", "Petrol", (70, 100, 120, 255)),
    CollisionMaterial("FRESH_MEAT", "Fresh Meat", (255, 55, 20, 255)),
    CollisionMaterial("DRIED_MEAT", "Dried Meat", (185, 100, 85, 255)),
    CollisionMaterial("EMISSIVE_GLASS", "Emissive Glass",
                      (205, 240, 255, 255)),
    CollisionMaterial("EMISSIVE_PLASTIC", "Emissive Plastic",
                      (255, 250, 210, 255)),
    CollisionMaterial("VFX_METAL_ELECTRIFIED",
                      "Vfx Metal Electrified", (155, 180, 190, 255)),
    CollisionMaterial("VFX_METAL_WATER_TOWER",
                      "Vfx Metal Water Tower", (155, 180, 190, 255)),
    CollisionMaterial("VFX_METAL_STEAM", "Vfx Metal Steam",
                      (155, 180, 190, 255)),
    CollisionMaterial("VFX_METAL_FLAME", "Vfx Metal Flame",
                      (155, 180, 190, 255)),
    CollisionMaterial("PHYS_NO_FRICTION", "Phys No Friction", (0, 0, 0, 255)),
    CollisionMaterial("PHYS_GOLF_BALL", "Phys Golf Ball", (0, 0, 0, 255)),
    CollisionMaterial("PHYS_TENNIS_BALL", "Phys Tennis Ball", (0, 0, 0, 255)),
    CollisionMaterial("PHYS_CASTER", "Phys Caster", (0, 0, 0, 255)),
    CollisionMaterial("PHYS_CASTER_RUSTY",
                      "Phys Caster Rusty", (0, 0, 0, 255)),
    CollisionMaterial("PHYS_CAR_VOID", "Phys Car Void", (0, 0, 0, 255)),
    CollisionMaterial("PHYS_PED_CAPSULE", "Phys Ped Capsule", (0, 0, 0, 255)),
    CollisionMaterial("PHYS_ELECTRIC_FENCE",
                      "Phys Electric Fence", (0, 0, 0, 255)),
    CollisionMaterial("PHYS_ELECTRIC_METAL",
                      "Phys Electric Metal", (0, 0, 0, 255)),
    CollisionMaterial("PHYS_BARBED_WIRE", "Phys Barbed Wire", (0, 0, 0, 255)),
    CollisionMaterial("PHYS_POOLTABLE_SURFACE",
                      "Phys Pooltable Surface", (155, 130, 95, 255)),
    CollisionMaterial("PHYS_POOLTABLE_CUSHION",
                      "Phys Pooltable Cushion", (155, 130, 95, 255)),
    CollisionMaterial("PHYS_POOLTABLE_BALL",
                      "Phys Pooltable Ball", (255, 250, 210, 255)),
    CollisionMaterial("BUTTOCKS", "Buttocks", (0, 0, 0, 255)),
    CollisionMaterial("THIGH_LEFT", "Thigh Left", (0, 0, 0, 255)),
    CollisionMaterial("SHIN_LEFT", "Shin Left", (0, 0, 0, 255)),
    CollisionMaterial("FOOT_LEFT", "Foot Left", (0, 0, 0, 255)),
    CollisionMaterial("THIGH_RIGHT", "Thigh Right", (0, 0, 0, 255)),
    CollisionMaterial("SHIN_RIGHT", "Shin Right", (0, 0, 0, 255)),
    CollisionMaterial("FOOT_RIGHT", "Foot Right", (0, 0, 0, 255)),
    CollisionMaterial("SPINE0", "Spine0", (0, 0, 0, 255)),
    CollisionMaterial("SPINE1", "Spine1", (0, 0, 0, 255)),
    CollisionMaterial("SPINE2", "Spine2", (0, 0, 0, 255)),
    CollisionMaterial("SPINE3", "Spine3", (0, 0, 0, 255)),
    CollisionMaterial("CLAVICLE_LEFT", "Clavicle Left", (0, 0, 0, 255)),
    CollisionMaterial("UPPER_ARM_LEFT", "Upper Arm Left", (0, 0, 0, 255)),
    CollisionMaterial("LOWER_ARM_LEFT", "Lower Arm Left", (0, 0, 0, 255)),
    CollisionMaterial("HAND_LEFT", "Hand Left", (0, 0, 0, 255)),
    CollisionMaterial("CLAVICLE_RIGHT", "Clavicle Right", (0, 0, 0, 255)),
    CollisionMaterial("UPPER_ARM_RIGHT", "Upper Arm Right", (0, 0, 0, 255)),
    CollisionMaterial("LOWER_ARM_RIGHT", "Lower Arm Right", (0, 0, 0, 255)),
    CollisionMaterial("HAND_RIGHT", "Hand Right", (0, 0, 0, 255)),
    CollisionMaterial("NECK", "Neck", (0, 0, 0, 255)),
    CollisionMaterial("HEAD", "Head", (0, 0, 0, 255)),
    CollisionMaterial("ANIMAL_DEFAULT", "Animal Default", (0, 0, 0, 255)),
    CollisionMaterial("CAR_ENGINE", "Car Engine", (255, 255, 255, 255)),
    CollisionMaterial("PUDDLE", "Puddle", (55, 145, 230, 255)),
    CollisionMaterial("CONCRETE_PAVEMENT",
                      "Concrete Pavement", (145, 145, 145, 255)),
    CollisionMaterial("BRICK_PAVEMENT", "Brick Pavement", (195, 95, 30, 255)),
    CollisionMaterial("PHYS_DYNAMIC_COVER_BOUND",
                      "Phys Dynamic Cover Bound", (0, 0, 0, 255)),
    CollisionMaterial("VFX_WOOD_BEER_BARREL",
                      "Vfx Wood Beer Barrel", (155, 130, 95, 255)),
    CollisionMaterial("WOOD_HIGH_FRICTION",
                      "Wood High Friction", (155, 130, 95, 255)),
    CollisionMaterial("ROCK_NOINST", "Rock Noinst", (185, 185, 185, 255)),
    CollisionMaterial("BUSHES_NOINST", "Bushes Noinst", (85, 160, 30, 255)),
    CollisionMaterial("METAL_SOLID_ROAD_SURFACE",
                      "Metal Solid Road Surface", (155, 180, 190, 255)),
    CollisionMaterial("STUNT_RAMP_SURFACE",
                      "Stunt Ramp Surface", (155, 180, 190, 255)),
    CollisionMaterial("TEMP_01", "Temp 01", (255, 0, 255, 255)),
    CollisionMaterial("TEMP_02", "Temp 02", (255, 0, 255, 255)),
]

conversionMap = {}
conversionMap[12667] = 0
conversionMap[3117] = 1
conversionMap[3117] = 1
conversionMap[3117] = 1
conversionMap[17263] = 4
conversionMap[17263] = 4
conversionMap[17263] = 4
conversionMap[3117] = 1
conversionMap[17263] = 1
conversionMap[29771] = 9
conversionMap[27481] = 10
conversionMap[8538] = 11
conversionMap[26554] = 12
conversionMap[30743] = 13
conversionMap[10369] = 14
conversionMap[31765] = 15
conversionMap[23858] = 16
conversionMap[8651] = 17
conversionMap[28241] = 18
conversionMap[28241] = 18
conversionMap[14664] = 20
conversionMap[28241] = 18
conversionMap[25172] = 22
conversionMap[16376] = 23
conversionMap[16836] = 24
conversionMap[19847] = 25
conversionMap[19847] = 25
conversionMap[6015] = 27
conversionMap[6015] = 27
conversionMap[2349] = 29
conversionMap[6015] = 27
conversionMap[30768] = 31
conversionMap[5937] = 32
conversionMap[31704] = 33
conversionMap[5937] = 32
conversionMap[29399] = 35
conversionMap[12756] = 36
conversionMap[11353] = 37
conversionMap[30007] = 38
conversionMap[30007] = 38
conversionMap[31485] = 40
conversionMap[29584] = 41
conversionMap[19519] = 42
conversionMap[1215] = 43
conversionMap[5825] = 44
conversionMap[21540] = 45
conversionMap[7477] = 46
conversionMap[29149] = 47
conversionMap[2804] = 48
conversionMap[19579] = 49
conversionMap[9975] = 50
conversionMap[19230] = 51
conversionMap[10801] = 52
conversionMap[6229] = 53
conversionMap[12264] = 54
conversionMap[4915] = 55
conversionMap[1588] = 56
conversionMap[7840] = 57
conversionMap[16286] = 58
conversionMap[9937] = 59
conversionMap[14082] = 60
conversionMap[8919] = 61
conversionMap[8919] = 61
conversionMap[13094] = 63
conversionMap[27653] = 64
conversionMap[7942] = 65
conversionMap[27872] = 66
conversionMap[10560] = 67
conversionMap[27872] = 66
conversionMap[11177] = 69
conversionMap[32350] = 70
conversionMap[3621] = 71
conversionMap[24105] = 72
conversionMap[5968] = 73
conversionMap[26590] = 74
conversionMap[7203] = 75
conversionMap[18359] = 76
conversionMap[3610] = 77
conversionMap[28698] = 78
conversionMap[3621] = 71
conversionMap[3886] = 80
conversionMap[1154] = 81
conversionMap[27285] = 82
conversionMap[27285] = 82
conversionMap[20949] = 84
conversionMap[28013] = 85
conversionMap[7615] = 86
conversionMap[9663] = 87
conversionMap[13894] = 88
conversionMap[7615] = 86
conversionMap[9663] = 87
conversionMap[13894] = 91
conversionMap[20949] = 84
conversionMap[14032] = 93
conversionMap[14032] = 93
conversionMap[26830] = 95
conversionMap[14032] = 93
conversionMap[28734] = 97
conversionMap[12009] = 98
conversionMap[12009] = 98
conversionMap[8010] = 100
conversionMap[17448] = 101
conversionMap[13438] = 102
conversionMap[28972] = 103
conversionMap[28972] = 103
conversionMap[28972] = 103
conversionMap[30262] = 106
conversionMap[21436] = 107
conversionMap[26830] = 95
conversionMap[9051] = 109
conversionMap[20949] = 110
conversionMap[25742] = 111
conversionMap[31555] = 112
conversionMap[27458] = 113
conversionMap[20949] = 110
conversionMap[30482] = 115
conversionMap[10560] = 116
conversionMap[25742] = 111
conversionMap[13254] = 118
conversionMap[6190] = 119
conversionMap[5414] = 120
conversionMap[22400] = 121
conversionMap[9200] = 122
conversionMap[19624] = 123
conversionMap[12714] = 124
conversionMap[30262] = 125
conversionMap[7888] = 126
conversionMap[21486] = 127
conversionMap[24688] = 128
conversionMap[23679] = 129
conversionMap[32495] = 130
conversionMap[25689] = 131
conversionMap[1356] = 132
conversionMap[12375] = 133
conversionMap[2642] = 134
conversionMap[31685] = 135
conversionMap[2485] = 136
conversionMap[25663] = 137
conversionMap[25663] = 137
conversionMap[25663] = 137
conversionMap[19811] = 140
conversionMap[19811] = 140
conversionMap[10421] = 142
conversionMap[30603] = 143
conversionMap[28722] = 144
conversionMap[28722] = 144
conversionMap[12596] = 146
conversionMap[25663] = 137
conversionMap[25663] = 137
conversionMap[25663] = 137
conversionMap[22716] = 150
conversionMap[18956] = 151
conversionMap[31978] = 152
conversionMap[29553] = 153
conversionMap[12086] = 154
conversionMap[18782] = 155
conversionMap[30123] = 156
conversionMap[13411] = 157
conversionMap[13412] = 158
conversionMap[13413] = 159
conversionMap[13414] = 160
conversionMap[28739] = 161
conversionMap[14792] = 162
conversionMap[6968] = 163
conversionMap[10833] = 164
conversionMap[14375] = 165
conversionMap[25907] = 166
conversionMap[23702] = 167
conversionMap[9227] = 168
conversionMap[10827] = 169
conversionMap[18961] = 170
conversionMap[7889] = 171
conversionMap[22401] = 172
conversionMap[21619] = 173
conversionMap[31765] = 174
conversionMap[6914] = 175
conversionMap[22716] = 176
conversionMap[17974] = 177
conversionMap[3886] = 178
conversionMap[27912] = 179
conversionMap[9975] = 180
conversionMap[1588] = 181
conversionMap[12667] = 0
conversionMap[23283] = 71 # DACH > WOOD_large
conversionMap[31694] = 23 # NAZWÓZ > SAND
conversionMap[15550] = 0 #PHYS_BLOCKER
conversionMap[20764] = 100 #GRAIN_SACK > CLOTH
conversionMap[17870] = 70 #WOOD_RAILROAD > WOOD_medium


def create_collision_material_from_index(collisionindex: int):

    if collisionindex in conversionMap:
       collisionindex = conversionMap[collisionindex]
    else:
        print(collisionindex)
        collisionindex = 0      

    matinfo = collisionmats[collisionindex]

    mat = bpy.data.materials.new(matinfo.name)
    mat.sollum_type = MaterialType.COLLISION
    mat.collision_properties.collision_index = collisionindex
    mat.use_nodes = True
    r = matinfo.color[0] / 255
    g = matinfo.color[1] / 255
    b = matinfo.color[2] / 255
    mat.node_tree.nodes["Principled BSDF"].inputs[0].default_value = (
r, g, b, 1)

    return mat
