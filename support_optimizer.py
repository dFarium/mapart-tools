from litemapy import Schematic, BlockState

def load_schematic_region(file_path):
    try:
        schem = Schematic.load(file_path)
        reg = list(schem.regions.values())[0]
    except FileNotFoundError:
        print("Schematic not found.")
        exit()
    return reg, schem

def replace_concrete_with_powder(file_path=""):
    reg,schem = load_schematic_region(file_path)
    leaves = BlockState("minecraft:mangrove_leaves")
    air = BlockState("minecraft:air")
    for x,y,z in reg.allblockpos():
        #si es concreto reemplazar por polvo y poner hojas abajo
        if reg.getblock(x,y,z).blockid.endswith("_concrete"):
            replacement = BlockState(reg.getblock(x,y,z).blockid + "_powder")
            #poner hojas solo si es mayor o igual a 1
            reg.setblock(x,y,z,replacement)
            if y >= 1:
                reg.setblock(x,y-1,z,leaves)

    schem.save(file_path)
    print("Concrete replaced.")

def remove_slab_supports(support_block="minecraft:cobblestone",file_path=""):
    reg,schem = load_schematic_region(file_path)
    air = BlockState("minecraft:air")
    for x,y,z in reg.allblockpos():
        if reg.getblock(x,y,z).blockid.endswith("_slab"):
            print("si funca")
            if y >= 1:
                if reg.getblock(x,y-1,z).blockid == support_block:
                    reg.setblock(x,y-1,z,air)
    schem.save(file_path)
    print("Slab supports removed.")