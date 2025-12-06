import pefile

sample= r"C:\Users\david\OneDrive\Documents\Lab 6\Procmon.exe"
pe = pefile.PE(sample)

print("The Entry point:", hex(pe.OPTIONAL_HEADER.AddressOfEntryPoint))
print("The Image Base:", hex(pe.OPTIONAL_HEADER.ImageBase))
print("The Number of Sections:", pe.FILE_HEADER.NumberOfSections)

print("\nImports:")
for entry in pe.DIRECTORY_ENTRY_IMPORT:
    dll_name = entry.dll.decode()
    print(" ", dll_name)
    for imp in entry.imports[:5]:
        print("     -", imp.name.decode() if imp.name else "None") 