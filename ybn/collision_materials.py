import bpy
from ..sollumz_properties import MaterialType
from collections import namedtuple

CollisionMaterial = namedtuple("CollisionMaterial", "name, ui_name, color")

collisionmats = [
    CollisionMaterial("DEFAULT", "Default", (213, 70, 223, 255)),
    CollisionMaterial("CONCRETE", "Concrete", (29, 34, 63, 255)),
    CollisionMaterial("CONCRETE_PAVEMENT", "Concrete Pavement", (216, 225, 53, 255)),
    CollisionMaterial("TARMAC", "Tarmac", (154, 8, 216, 255)),
    CollisionMaterial("ROCK", "Rock", (204, 85, 203, 255)),
    CollisionMaterial("ROCK_MOSSY", "Rock Mossy", (137, 84, 168, 255)),
    CollisionMaterial("STONE", "Stone", (5, 225, 150, 255)),
    CollisionMaterial("COBBLESTONE", "Cobblestone", (3, 97, 58, 255)),
    CollisionMaterial("COBBLESTONE_DIRT", "Cobblestone Dirt", (98, 93, 134, 255)),
    CollisionMaterial("BRICK", "Brick", (3, 69, 166, 255)),
    CollisionMaterial("BRICK_PAVEMENT", "Brick Pavement", (32, 43, 41, 255)),
    CollisionMaterial("MARBLE", "Marble", (14, 116, 216, 255)),
    CollisionMaterial("SANDSTONE_SOLID", "Sandstone Solid", (31, 194, 135, 255)),
    CollisionMaterial("SANDSTONE_BRITTLE", "Sandstone Brittle", (1, 217, 95, 255)),
    CollisionMaterial("SAND_COMPACT", "Sand Compact", (221, 118, 234, 255)),
    CollisionMaterial("SAND_WET", "Sand Wet", (34, 17, 121, 255)),
    CollisionMaterial("SAND_DRY_DEEP", "Sand Dry Deep", (54, 246, 26, 255)),
    CollisionMaterial("SAND_WET_DEEP", "Sand Wet Deep", (161, 151, 111, 255)),
    CollisionMaterial("QUICKSAND", "Quicksand", (110, 136, 224, 255)),
    CollisionMaterial("ALGAE", "Algae", (185, 22, 223, 255)),
    CollisionMaterial("ALGAE_THICK", "Algae Thick", (147, 12, 85, 255)),
    CollisionMaterial("TAR_PIT", "Tar Pit", (51, 114, 108, 255)),
    CollisionMaterial("ICE", "Ice", (92, 15, 11, 255)),
    CollisionMaterial("SNOW_COMPACT", "Snow Compact", (230, 145, 66, 255)),
    CollisionMaterial("SNOW_DEEP", "Snow Deep", (118, 105, 120, 255)),
    CollisionMaterial("SLUSH", "Slush", (154, 116, 45, 255)),
    CollisionMaterial("GRAVEL_SMALL", "Gravel Small", (3, 182, 198, 255)),
    CollisionMaterial("GRAVEL_LARGE", "Gravel Large", (141, 243, 70, 255)),
    CollisionMaterial("GRAVEL_WET", "Gravel Wet", (114, 204, 158, 255)),
    CollisionMaterial("GRAVEL_DEEP", "Gravel Deep", (109, 122, 145, 255)),
    CollisionMaterial("GRAVEL_MUDDY", "Gravel Muddy", (190, 60, 59, 255)),
    CollisionMaterial("GRAVEL_MUDDY_DEEP", "Gravel Muddy Deep", (136, 206, 37, 255)),
    CollisionMaterial("GRAVEL_DIRT", "Gravel Dirt", (249, 7, 121, 255)),
    CollisionMaterial("GRAVEL_GRASS", "Gravel Grass", (73, 177, 73, 255)),
    CollisionMaterial("DIRT_TRACK", "Dirt Track", (159, 74, 66, 255)),
    CollisionMaterial("DIRT_TRACK_DEEP", "Dirt Track Deep", (13, 88, 14, 255)),
    CollisionMaterial("DIRT_GRASS", "Dirt Grass", (40, 127, 150, 255)),
    CollisionMaterial("MUD_HARD", "Mud Hard", (139, 11, 250, 255)),
    CollisionMaterial("MUD_POTHOLE", "Mud Pothole", (163, 86, 251, 255)),
    CollisionMaterial("MUD_SOFT", "Mud Soft", (113, 234, 145, 255)),
    CollisionMaterial("MUD_UNDERWATER", "Mud Underwater", (14, 139, 43, 255)),
    CollisionMaterial("MUD_DEEP", "Mud Deep", (91, 183, 205, 255)),
    CollisionMaterial("MARSH", "Marsh", (189, 234, 2, 255)),
    CollisionMaterial("MARSH_DEEP", "Marsh Deep", (190, 240, 0, 255)),
    CollisionMaterial("SOIL", "Soil", (131, 52, 74, 255)),
    CollisionMaterial("SOIL_DEEP", "Soil Deep", (233, 185, 192, 255)),
    CollisionMaterial("CLAY_HARD", "Clay Hard", (54, 123, 231, 255)),
    CollisionMaterial("CLAY_SOFT", "Clay Soft", (229, 246, 97, 255)),
    CollisionMaterial("ASH", "Ash", (239, 234, 81, 255)),
    CollisionMaterial("COAL", "Coal", (13, 160, 174, 255)),
    CollisionMaterial("MANURE", "Manure", (107, 126, 148, 255)),
    CollisionMaterial("MOSS", "Moss", (95, 131, 109, 255)),
    CollisionMaterial("MOSS_DEEP", "Moss Deep", (42, 124, 180, 255)),
    CollisionMaterial("GRASS_DEAD", "Grass Dead", (193, 18, 255, 255)),
    CollisionMaterial("GRASS_LUSH", "Grass Lush", (23, 160, 113, 255)),
    CollisionMaterial("GRASS_LONG", "Grass Long", (183, 92, 0, 255)),
    CollisionMaterial("GRASS", "Grass", (148, 51, 98, 255)),
    CollisionMaterial("GRASS_SHORT", "Grass Short", (13, 245, 144, 255)),
    CollisionMaterial("HAY", "Hay", (140, 218, 127, 255)),
    CollisionMaterial("BUSHES", "Bushes", (181, 239, 188, 255)),
    CollisionMaterial("SPARSE_BUSHES", "Sparse Bushes", (57, 16, 195, 255)),
    CollisionMaterial("DENSE_BUSHES", "Dense Bushes", (156, 195, 226, 255)),
    CollisionMaterial("TWIGS", "Twigs", (7, 251, 7, 255)),
    CollisionMaterial("PINE_NEEDLES", "Pine Needles", (38, 120, 85, 255)),
    CollisionMaterial("LEAVES_DRY", "Leaves Dry", (108, 248, 11, 255)),
    CollisionMaterial("LEAVES_TOBACCO", "Leaves Tobacco", (160, 239, 14, 255)),
    CollisionMaterial("LEAVES", "Leaves", (65, 22, 188, 255)),
    CollisionMaterial("LEAVES_MAPLE", "Leaves Maple", (156, 133, 231, 255)),
    CollisionMaterial("LEAVES_OAK", "Leaves Oak", (79, 205, 139, 255)),
    CollisionMaterial("LEAVES_FICUS", "Leaves Ficus", (24, 208, 227, 255)),
    CollisionMaterial("WOODCHIPS", "Woodchips", (79, 129, 56, 255)),
    CollisionMaterial("TREE_PINE", "Tree Pine", (193, 227, 231, 255)),
    CollisionMaterial("TREE_PINE_SNOW", "Tree Pine Snow", (154, 224, 92, 255)),
    CollisionMaterial("FLOWERS", "Flowers", (136, 146, 194, 255)),
    CollisionMaterial("CROP_HUSK", "Crop Husk", (67, 110, 17, 255)),
    CollisionMaterial("TREE_BARK", "Tree Bark", (21, 18, 2, 255)),
    CollisionMaterial("CACTUS", "Cactus", (47, 53, 41, 255)),
    CollisionMaterial("METAL_SOLID_SMALL", "Metal Solid Small", (91, 191, 22, 255)),
    CollisionMaterial("METAL_SOLID_MEDIUM", "Metal Solid Medium", (221, 98, 223, 255)),
    CollisionMaterial("METAL_SOLID_LARGE", "Metal Solid Large", (116, 118, 6, 255)),
    CollisionMaterial("METAL_HOLLOW_SMALL", "Metal Hollow Small", (83, 21, 207, 255)),
    CollisionMaterial("METAL_HOLLOW_MEDIUM", "Metal Hollow Medium", (82, 50, 0, 255)),
    CollisionMaterial("METAL_HOLLOW_LARGE", "Metal Hollow Large", (145, 9, 49, 255)),
    CollisionMaterial("METAL_CHAINLINK_SMALL", "Metal Chainlink Small", (101, 19, 249, 255)),
    CollisionMaterial("METAL_CORRUGATED_IRON", "Metal Corrugated Iron", (68, 147, 221, 255)),
    CollisionMaterial("METAL_GRILLE", "Metal Grille", (68, 132, 43, 255)),
    CollisionMaterial("METAL_RAILING", "Metal Railing", (50, 23, 172, 255)),
    CollisionMaterial("METAL_RAILING_TRAM", "Metal Railing Tram", (20, 74, 36, 255)),
    CollisionMaterial("METAL_DUCT", "Metal Duct", (51, 143, 92, 255)),
    CollisionMaterial("METAL_PENETRABLE", "Metal Penetrable", (37, 13, 73, 255)),
    CollisionMaterial("METAL_BARS", "Metal Bars", (133, 14, 130, 255)),
    CollisionMaterial("WOOD_ROOF", "Wood Roof", (172, 112, 6, 255)),
    CollisionMaterial("WOOD_BURNING", "Wood Burning", (190, 54, 236, 255)),
    CollisionMaterial("WOOD_BURNT", "Wood Burnt", (42, 177, 254, 255)),
    CollisionMaterial("WOOD_CHIPS", "Wood Chips", (145, 184, 155, 255)),
    CollisionMaterial("WOOD_SOLID_SMALL", "Wood Solid Small", (200, 123, 232, 255)),
    CollisionMaterial("WOOD_SOLID_MEDIUM", "Wood Solid Medium", (146, 187, 171, 255)),
    CollisionMaterial("WOOD_SOLID_LARGE", "Wood Solid Large", (6, 0, 84, 255)),
    CollisionMaterial("WOOD_SOLID_POLISHED", "Wood Solid Polished", (36, 162, 183, 255)),
    CollisionMaterial("WOOD_FLOOR_DUSTY", "Wood Floor Dusty", (24, 211, 214, 255)),
    CollisionMaterial("WOOD_HOLLOW_SMALL", "Wood Hollow Small", (213, 132, 112, 255)),
    CollisionMaterial("WOOD_HOLLOW_MEDIUM", "Wood Hollow Medium", (25, 244, 246, 255)),
    CollisionMaterial("WOOD_HOLLOW_LARGE", "Wood Hollow Large", (96, 165, 207, 255)),
    CollisionMaterial("WOOD_OLD_CREAKY", "Wood Old Creaky", (201, 202, 231, 255)),
    CollisionMaterial("WOOD_LATTICE", "Wood Lattice", (156, 159, 188, 255)),
    CollisionMaterial("WOOD_PENETRABLE", "Wood Penetrable", (64, 124, 248, 255)),
    CollisionMaterial("CERAMIC", "Ceramic", (101, 241, 220, 255)),
    CollisionMaterial("ROOF_TILE", "Roof Tile", (238, 140, 125, 255)),
    CollisionMaterial("TARPAULIN", "Tarpaulin", (149, 135, 211, 255)),
    CollisionMaterial("PLASTIC_CLEAR", "Plastic Clear", (142, 103, 228, 255)),
    CollisionMaterial("PLASTIC_HOLLOW_CLEAR", "Plastic Hollow Clear", (9, 188, 8, 255)),
    CollisionMaterial("PLASTIC_HIGH_DENSITY_CLEAR", "Plastic High Density Clear", (19, 132, 158, 255)),
    CollisionMaterial("RUBBER", "Rubber", (5, 212, 152, 255)),
    CollisionMaterial("CARPET_SOLID", "Carpet Solid", (2, 26, 146, 255)),
    CollisionMaterial("CARPET_SOLID_DUSTY", "Carpet Solid Dusty", (77, 250, 20, 255)),
    CollisionMaterial("CLOTH", "Cloth", (76, 249, 81, 255)),
    CollisionMaterial("CLOTH_SACK", "Cloth Sack", (117, 73, 51, 255)),
    CollisionMaterial("PLASTER_SOLID", "Plaster Solid", (99, 168, 150, 255)),
    CollisionMaterial("PLASTER_BRITTLE", "Plaster Brittle", (251, 191, 68, 255)),
    CollisionMaterial("PLASTER_PENETRABLE", "Plaster Penetrable", (42, 57, 245, 255)),
    CollisionMaterial("PAPER", "Paper", (46, 169, 102, 255)),
    CollisionMaterial("FEATHER_PILLOW", "Feather Pillow", (116, 157, 127, 255)),
    CollisionMaterial("LEATHER", "Leather", (117, 201, 61, 255)),
    CollisionMaterial("SLATTED_BLINDS", "Slatted Blinds", (170, 35, 99, 255)),
    CollisionMaterial("UPHOLSTRY", "Upholstry", (174, 172, 152, 255)),
    CollisionMaterial("CURTAINS", "Curtains", (180, 248, 124, 255)),
    CollisionMaterial("WICKER", "Wicker", (140, 15, 221, 255)),
    CollisionMaterial("TERRACOTTA", "Terracotta", (224, 148, 83, 255)),
    CollisionMaterial("PORCELAIN", "Porcelain", (130, 18, 100, 255)),
    CollisionMaterial("TILE", "Tile", (70, 243, 178, 255)),
    CollisionMaterial("GRAIN_SACK", "Grain Sack", (22, 18, 252, 255)),
    CollisionMaterial("SAND_BAG", "Sand Bag", (179, 166, 214, 255)),
    CollisionMaterial("PAINT_CAN", "Paint Can", (3, 84, 9, 255)),
    CollisionMaterial("TRASH", "Trash", (25, 90, 67, 255)),
    CollisionMaterial("GLASS_SHOOT_THROUGH", "Glass Shoot Through", (66, 23, 55, 255)),
    CollisionMaterial("GLASS_BOTTLE_SHOT", "Glass Bottle Shot", (105, 198, 17, 255)),
    CollisionMaterial("GLASS_BOTTLE_MEDICINE", "Glass Bottle Medicine", (47, 94, 211, 255)),
    CollisionMaterial("GLASS_BOTTLE_LIQUOR", "Glass Bottle Liquor", (106, 28, 53, 255)),
    CollisionMaterial("GLASS_BOTTLE_JUG", "Glass Bottle Jug", (196, 203, 13, 255)),
    CollisionMaterial("GLASS_BULLETPROOF", "Glass Bulletproof", (208, 71, 49, 255)),
    CollisionMaterial("GLASS_BULLETPROOF_SEE_THROUGH", "Glass Bulletproof See Through", (194, 190, 108, 255)),
    CollisionMaterial("GLASS_OPAQUE", "Glass Opaque", (34, 247, 219, 255)),
    CollisionMaterial("CAR_METAL", "Car Metal", (103, 148, 63, 255)),
    CollisionMaterial("CAR_SOFTTOP", "Car Softtop", (118, 223, 135, 255)),
    CollisionMaterial("CAR_SOFTTOP_CLEAR", "Car Softtop Clear", (80, 214, 82, 255)),
    CollisionMaterial("CAR_GLASS_WEAK", "Car Glass Weak", (224, 253, 42, 255)),
    CollisionMaterial("CAR_GLASS_MEDIUM", "Car Glass Medium", (59, 67, 186, 255)),
    CollisionMaterial("CAR_GLASS_STRONG", "Car Glass Strong", (33, 10, 169, 255)),
    CollisionMaterial("CAR_GLASS_BULLETPROOF", "Car Glass Bulletproof", (248, 135, 99, 255)),
    CollisionMaterial("CAR_GLASS_OPAQUE", "Car Glass Opaque", (241, 182, 185, 255)),
    CollisionMaterial("CAR_ENGINE", "Car Engine", (10, 237, 111, 255)),
    CollisionMaterial("VEH_WOOD", "Veh Wood", (54, 122, 179, 255)),
    CollisionMaterial("WEAPON_WOOD", "Weapon Wood", (7, 152, 109, 255)),
    CollisionMaterial("WEAPON_METAL", "Weapon Metal", (50, 83, 87, 255)),
    CollisionMaterial("WATER_SHALLOW", "Water Shallow", (79, 89, 133, 255)),
    CollisionMaterial("WATER", "Water", (118, 150, 221, 255)),
    CollisionMaterial("BLOOD", "Blood", (248, 88, 29, 255)),
    CollisionMaterial("OIL", "Oil", (120, 21, 121, 255)),
    CollisionMaterial("PETROL", "Petrol", (121, 98, 56, 255)),
    CollisionMaterial("PUDDLE", "Puddle", (254, 116, 13, 255)),
    CollisionMaterial("PUDDLE_ANKLE", "Puddle Ankle", (128, 21, 35, 255)),
    CollisionMaterial("WATER_ANKLE", "Water Ankle", (198, 174, 22, 255)),
    CollisionMaterial("WATER_SHIN", "Water Shin", (252, 229, 150, 255)),
    CollisionMaterial("WATER_KNEE", "Water Knee", (28, 15, 77, 255)),
    CollisionMaterial("FRESH_MEAT", "Fresh Meat", (64, 188, 20, 255)),
    CollisionMaterial("DRIED_MEAT", "Dried Meat", (160, 97, 161, 255)),
    CollisionMaterial("FURRY_MEAT", "Furry Meat", (187, 212, 186, 255)),
    CollisionMaterial("PELT_FUR", "Pelt Fur", (249, 18, 189, 255)),
    CollisionMaterial("LEATHER_HIDE", "Leather Hide", (89, 219, 236, 255)),
    CollisionMaterial("BONES", "Bones", (227, 149, 18, 255)),
    CollisionMaterial("EMISSIVE_GLASS", "Emissive Glass", (252, 65, 201, 255)),
    CollisionMaterial("EMISSIVE_PLASTIC", "Emissive Plastic", (200, 154, 233, 255)),
    CollisionMaterial("VFX_METAL_ELECTRIFIED", "Vfx Metal Electrified", (171, 206, 224, 255)),
    CollisionMaterial("VFX_METAL_WATER_TOWER", "Vfx Metal Water Tower", (208, 217, 131, 255)),
    CollisionMaterial("VFX_WOOD_BEER_BARREL", "Vfx Wood Beer Barrel", (186, 214, 67, 255)),
    CollisionMaterial("VFX_METAL_STEAM", "Vfx Metal Steam", (214, 28, 60, 255)),
    CollisionMaterial("VFX_METAL_FLAME", "Vfx Metal Flame", (79, 170, 77, 255)),
    CollisionMaterial("PHYS_NO_FRICTION", "Phys No Friction", (145, 105, 140, 255)),
    CollisionMaterial("PHYS_CASTER", "Phys Caster", (86, 40, 171, 255)),
    CollisionMaterial("PHYS_CAR_VOID", "Phys Car Void", (235, 96, 219, 255)),
    CollisionMaterial("PHYS_PED_CAPSULE", "Phys Ped Capsule", (242, 129, 201, 255)),
    CollisionMaterial("PHYS_MACHINERY", "Phys Machinery", (150, 129, 14, 255)),
    CollisionMaterial("PHYS_BARBED_WIRE", "Phys Barbed Wire", (31, 24, 20, 255)),
    CollisionMaterial("PHYS_BLOCKER", "Phys Blocker", (232, 56, 231, 255)),
    CollisionMaterial("PHYS_DYNAMIC_COVER_BOUND", "Phys Dynamic Cover Bound", (61, 118, 195, 255)),
    CollisionMaterial("BUTTOCKS", "Buttocks", (49, 37, 215, 255)),
    CollisionMaterial("THIGH_LEFT", "Thigh Left", (43, 236, 32, 255)),
    CollisionMaterial("SHIN_LEFT", "Shin Left", (142, 80, 193, 255)),
    CollisionMaterial("FOOT_LEFT", "Foot Left", (104, 95, 50, 255)),
    CollisionMaterial("THIGH_RIGHT", "Thigh Right", (231, 65, 32, 255)),
    CollisionMaterial("SHIN_RIGHT", "Shin Right", (220, 135, 140, 255)),
    CollisionMaterial("FOOT_RIGHT", "Foot Right", (154, 171, 233, 255)),
    CollisionMaterial("SPINE0", "Spine0", (193, 200, 37, 255)),
    CollisionMaterial("SPINE1", "Spine1", (125, 244, 3, 255)),
    CollisionMaterial("SPINE2", "Spine2", (218, 1, 178, 255)),
    CollisionMaterial("SPINE3", "Spine3", (56, 44, 225, 255)),
    CollisionMaterial("CLAVICLE_LEFT", "Clavicle Left", (49, 187, 40, 255)),
    CollisionMaterial("UPPER_ARM_LEFT", "Upper Arm Left", (152, 136, 6, 255)),
    CollisionMaterial("LOWER_ARM_LEFT", "Lower Arm Left", (157, 233, 14, 255)),
    CollisionMaterial("HAND_LEFT", "Hand Left", (199, 54, 216, 255)),
    CollisionMaterial("CLAVICLE_RIGHT", "Clavicle Right", (42, 230, 228, 255)),
    CollisionMaterial("UPPER_ARM_RIGHT", "Upper Arm Right", (68, 5, 114, 255)),
    CollisionMaterial("LOWER_ARM_RIGHT", "Lower Arm Right", (153, 10, 170, 255)),
    CollisionMaterial("HAND_RIGHT", "Hand Right", (226, 49, 194, 255)),
    CollisionMaterial("NECK", "Neck", (197, 101, 103, 255)),
    CollisionMaterial("HEAD", "Head", (81, 63, 83, 255)),
    CollisionMaterial("ANIMAL_DEFAULT", "Animal Default", (113, 110, 30, 255)),
    CollisionMaterial("PROP_ROCK", "Prop Rock", (103, 79, 193, 255)),
    CollisionMaterial("PROP_STONE", "Prop Stone", (176, 174, 204, 255)),
    CollisionMaterial("TAR_PAPER", "Tar Paper", (60, 33, 222, 255)),
    CollisionMaterial("AM_BASE_WOOD_RAILROAD", "Am Base Wood Railroad", (254, 245, 167, 255)),
    CollisionMaterial("WOOD_RAILROAD", "Wood Railroad", (8, 127, 90, 255)),
    CollisionMaterial("BONE_LIGHT", "Bone Light", (241, 43, 75, 255)),
    CollisionMaterial("BONE_HEAVY", "Bone Heavy", (52, 25, 24, 255)),
    CollisionMaterial("WOOD_ROTTEN", "Wood Rotten", (12, 147, 178, 255))
]

conversionMap = {}
conversionMap[12667] = 0
conversionMap[3117] = 1
conversionMap[3117] = 2
conversionMap[3117] = 3
conversionMap[17263] = 4
conversionMap[17263] = 5
conversionMap[17263] = 6
conversionMap[3117] = 7
conversionMap[17263] = 8
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
conversionMap[28241] = 19
conversionMap[14664] = 20
conversionMap[28241] = 21
conversionMap[25172] = 22
conversionMap[16376] = 23
conversionMap[16836] = 24
conversionMap[19847] = 25
conversionMap[19847] = 26
conversionMap[6015] = 27
conversionMap[6015] = 28
conversionMap[2349] = 29
conversionMap[6015] = 30
conversionMap[30768] = 31
conversionMap[5937] = 32
conversionMap[31704] = 33
conversionMap[5937] = 34
conversionMap[29399] = 35
conversionMap[12756] = 36
conversionMap[11353] = 37
conversionMap[30007] = 38
conversionMap[30007] = 39
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
conversionMap[8919] = 62
conversionMap[13094] = 63
conversionMap[27653] = 64
conversionMap[7942] = 65
conversionMap[27872] = 66
conversionMap[10560] = 67
conversionMap[27872] = 68
conversionMap[11177] = 69
conversionMap[32350] = 70
conversionMap[3621] = 71
conversionMap[24105] = 72
conversionMap[5968] = 73
conversionMap[26590] = 74
conversionMap[7203] = 75
conversionMap[18359] = 76
conversionMap[3886] = 77
conversionMap[28698] = 78
conversionMap[3621] = 79
conversionMap[3886] = 80
conversionMap[1154] = 81
conversionMap[27285] = 82
conversionMap[27285] = 83
conversionMap[20949] = 84
conversionMap[28013] = 85
conversionMap[7615] = 86
conversionMap[9663] = 87
conversionMap[13894] = 88
conversionMap[7615] = 89
conversionMap[9663] = 90
conversionMap[13894] = 91
conversionMap[20949] = 92
conversionMap[14032] = 93
conversionMap[14032] = 94
conversionMap[26830] = 95
conversionMap[14032] = 96
conversionMap[28734] = 97
conversionMap[12009] = 98
conversionMap[12009] = 99
conversionMap[8010] = 100
conversionMap[17448] = 101
conversionMap[13438] = 102
conversionMap[28972] = 103
conversionMap[28972] = 104
conversionMap[28972] = 105
conversionMap[30262] = 106
conversionMap[21436] = 107
conversionMap[26830] = 108
conversionMap[9051] = 109
conversionMap[20949] = 110
conversionMap[25742] = 111
conversionMap[31555] = 112
conversionMap[27458] = 113
conversionMap[20949] = 114
conversionMap[30482] = 115
conversionMap[10560] = 116
conversionMap[25742] = 117
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
conversionMap[25663] = 138
conversionMap[25663] = 139
conversionMap[19811] = 140
conversionMap[19811] = 141
conversionMap[10421] = 142
conversionMap[30603] = 143
conversionMap[28722] = 144
conversionMap[28722] = 145
conversionMap[12596] = 146
conversionMap[25663] = 147
conversionMap[25663] = 148
conversionMap[25663] = 149
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
conversionMap[12667] = 182


def create_collision_material_from_index(collisionindex: int):

    if collisionindex in conversionMap:
       collisionindex = conversionMap[collisionindex]
    else:
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
