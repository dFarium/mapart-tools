
from nbt.nbt import *
def fix_litematica_import(file_path):
    
    file = NBTFile(file_path, 'rb')
    schematic = file.tags[3].tags[0]
    schematic.tags.append(TAG_List(name="PendingBlockTicks", type = TAG_Compound))
    schematic.tags.append(TAG_List(name="PendingFluidTicks", type = TAG_Compound))
    file.write_file(file_path)
