from litemapy import Schematic, BlockState


schematic_name = "mere 1 - copia.litematic"
support_block = "minecraft:cobblestone"

CONCRETE_BLOCK_IDS = [
    "minecraft:white_concrete",
    "minecraft:orange_concrete",
    "minecraft:magenta_concrete",
    "minecraft:light_blue_concrete",
    "minecraft:yellow_concrete",
    "minecraft:lime_concrete",
    "minecraft:pink_concrete",
    "minecraft:gray_concrete",
    "minecraft:light_gray_concrete",
    "minecraft:cyan_concrete",
    "minecraft:purple_concrete",
    "minecraft:blue_concrete",
    "minecraft:brown_concrete",
    "minecraft:green_concrete",
    "minecraft:red_concrete",
    "minecraft:black_concrete"
]

CONCRETE_POWDER_IDS = [
    "minecraft:white_concrete_powder",
    "minecraft:orange_concrete_powder",
    "minecraft:magenta_concrete_powder",
    "minecraft:light_blue_concrete_powder",
    "minecraft:yellow_concrete_powder",
    "minecraft:lime_concrete_powder",
    "minecraft:pink_concrete_powder",
    "minecraft:gray_concrete_powder",
    "minecraft:light_gray_concrete_powder",
    "minecraft:cyan_concrete_powder",
    "minecraft:purple_concrete_powder",
    "minecraft:blue_concrete_powder",
    "minecraft:brown_concrete_powder",
    "minecraft:green_concrete_powder",
    "minecraft:red_concrete_powder",
    "minecraft:black_concrete_powder"
]

SLAB_IDS = [
    "minecraft:oak_slab",
    "minecraft:spruce_slab",
    "minecraft:birch_slab",
    "minecraft:jungle_slab",
    "minecraft:acacia_slab",
    "minecraft:dark_oak_slab",
    "minecraft:mangrove_slab",
    "minecraft:cherry_slab",
    "minecraft:bamboo_slab",
    "minecraft:bamboo_mosaic_slab",
    "minecraft:crimson_slab",
    "minecraft:warped_slab",
    "minecraft:stone_slab",
    "minecraft:smooth_stone_slab",
    "minecraft:granite_slab",
    "minecraft:polished_granite_slab",
    "minecraft:diorite_slab",
    "minecraft:polished_diorite_slab",
    "minecraft:andesite_slab",
    "minecraft:polished_andesite_slab",
    "minecraft:cobblestone_slab",
    "minecraft:mossy_cobblestone_slab",
    "minecraft:stone_brick_slab",
    "minecraft:mossy_stone_brick_slab",
    "minecraft:brick_slab",
    "minecraft:end_stone_brick_slab",
    "minecraft:nether_brick_slab",
    "minecraft:red_nether_brick_slab",
    "minecraft:sandstone_slab",
    "minecraft:cut_sandstone_slab",
    "minecraft:smooth_sandstone_slab",
    "minecraft:red_sandstone_slab",
    "minecraft:cut_red_sandstone_slab",
    "minecraft:smooth_red_sandstone_slab",
    "minecraft:quartz_slab",
    "minecraft:smooth_quartz_slab",
    "minecraft:purpur_slab",
    "minecraft:prismarine_slab",
    "minecraft:prismarine_brick_slab",
    "minecraft:dark_prismarine_slab",
    "minecraft:blackstone_slab",
    "minecraft:polished_blackstone_slab",
    "minecraft:polished_blackstone_brick_slab",
    "minecraft:cut_copper_slab",
    "minecraft:exposed_cut_copper_slab",
    "minecraft:weathered_cut_copper_slab",
    "minecraft:oxidized_cut_copper_slab",
    "minecraft:waxed_cut_copper_slab",
    "minecraft:waxed_exposed_cut_copper_slab",
    "minecraft:waxed_weathered_cut_copper_slab",
    "minecraft:waxed_oxidized_cut_copper_slab",
    "minecraft:cobbled_deepslate_slab",
    "minecraft:polished_deepslate_slab",
    "minecraft:deepslate_brick_slab",
    "minecraft:deepslate_tile_slab",
    "minecraft:mud_brick_slab"
    ]
try:
    schem = Schematic.load(schematic_name)
except FileNotFoundError:
    print("Schematic not found.")
    exit()

reg = list(schem.regions.values())[0]

def is_slab(block_id):
    if block_id in SLAB_IDS:
        return True

def replace_cobblestone_below_falling_blocks():
    for x,y,z in reg.allblockpos():
        if is_powder(reg.getblock(x,y,z).blockid):
            if y > 1:
                reg.setblock(x,y-1,z,BlockState("minecraft:jungle_leaves"))
            else:
                reg.setblock(x,y-1,z,BlockState("minecraft:air"))

def is_powder(block_id):
    powder_blocks = [
        "minecraft:white_concrete_powder",
        "minecraft:orange_concrete_powder",
        "minecraft:magenta_concrete_powder",
        "minecraft:light_blue_concrete_powder",
        "minecraft:yellow_concrete_powder",
        "minecraft:lime_concrete_powder",
        "minecraft:pink_concrete_powder",
        "minecraft:gray_concrete_powder",
        "minecraft:light_gray_concrete_powder",
        "minecraft:cyan_concrete_powder",
        "minecraft:purple_concrete_powder",
        "minecraft:blue_concrete_powder",
        "minecraft:brown_concrete_powder",
        "minecraft:green_concrete_powder",
        "minecraft:red_concrete_powder",
        "minecraft:black_concrete_powder",
        "minecraft:sand"
    ]
    if block_id in powder_blocks:
        return True
    else:
        return False

air = BlockState("minecraft:air")

for x,y,z in reg.allblockpos():
    if reg.getblock(x,y,z).blockid == "minecraft:cobblestone":
        if is_slab(reg.getblock(x,y+1,z).blockid):
            reg.setblock(x,y,z,air)

replace_cobblestone_below_falling_blocks()
            

schem.save(schematic_name)
print("Slab support removed from schematic.")


