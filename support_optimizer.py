from litemapy import Schematic, BlockState

def load_schematic_region(file_path):
    try:
        schem = Schematic.load(file_path)
        reg = list(schem.regions.values())[0]
    except FileNotFoundError:
        print("Schematic not found.")
        exit()
    return reg, schem

def powder_to_concrete(block_id):
    if is_powder(block_id):
        return POWDER_TO_CONCRETE[block_id]
    else:
        return block_id

def replace_concrete_with_powder(file_path=""):
    reg,schem = load_schematic_region(file_path)
    leaves = BlockState("minecraft:mangrove_leaves")
    air = BlockState("minecraft:air")
    for x,y,z in reg.allblockpos():
        #si es concreto reemplazar por polvo y poner hojas abajo
        if "_powder" in reg.getblock(x,y,z).blockid:
            replacement = BlockState(reg.getblock(x,y,z).blockid.replace("_powder",""))
            #poner hojas solo si es mayor a 1
            reg.setblock(x,y,z,replacement)
            if y >= 1:
                reg.setblock(x,y-1,z,leaves)
            else:
                reg.setblock(x,y-1,z,air)
    schem.save(file_path)
    print("Concrete replaced.")

def remove_slab_supports(support_block="minecraft:cobblestone",file_path=""):
    reg,schem = load_schematic_region(file_path)
    air = BlockState("minecraft:air")
    for x,y,z in reg.allblockpos():
        if "_slab" in reg.getblock(x,y,z).blockid:
            if y >= 1:
                if reg.getblock(x,y-1,z).blockid == support_block:
                    reg.setblock(x,y-1,z,air)
    schem.save(file_path)
    print("Slab supports removed.")