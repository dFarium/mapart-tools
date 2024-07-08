from nbt.nbt import *
def fix_litematica_import(file_path=""):
    try:
        file = NBTFile(file_path, 'rb')
    except FileNotFoundError:
        print("File not found.")
        exit()
    schematic = file.tags[3].tags[0]
    schematic.tags.append(TAG_List(name="PendingBlockTicks", type = TAG_Compound))
    schematic.tags.append(TAG_List(name="PendingFluidTicks", type = TAG_Compound))
    file.write_file(file_path)
    print("NBT data fixed")
