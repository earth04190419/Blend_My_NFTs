import platform

# NFT configurations:
maxNFTs = 0    # The maximum number of NFTs you want to generate - doesn't do anything yet
nftsPerBatch = 1   # Number of NFTs per batch
renderBatch = 1     # The batch number to render in PNG-Generator
imageName = "ThisCozyPlace_"    # The name of the NFT image produces by PNG-Generator
fileFormat = 'JPEG'     # The file format you want to export the NFT as.
                    # Visit https://docs.blender.org/api/current/bpy.types.Image.html#bpy.types.Image.file_format
                    # for a list of file formats supported by Blender. Enter the file extension exactly as specified in
                    # the Blender API documentation above.

includeRarity = False # True = include weighted rarity percentages in NFTRecord.json calculations,
                      # False = Pure random selection of variants

# The path to Blend_My_NFTs folder:
# Example mac: /Users/Path/to/Blend_My_NFTs
# Example windows: C:\Users\Path\to\Blend_My_NFTs
save_path_mac = '/Users/torrinleonard/Desktop/Blend_My_NFTs'
save_path_windows = r''

mac = 'Darwin' # Mac OS
windows = 'Windows' # Windows
slash = '' # Leave empty
save_path = None # Leave empty

# Save_path utilities and os compatibility
if platform.system() == mac:
    save_path = save_path_mac
    slash = '/'
elif platform.system() == windows:
    save_path = save_path_windows
    slash = '\\'

# Paths to folders
batch_path = save_path + slash + 'Batch_Json_files'
images_path = save_path + slash + 'NFT_Image_Output'