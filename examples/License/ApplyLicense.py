from aspose.threed import Scene, License, Metered

def UsingFile():
    # ExStart:ApplyLicenseUsingFile
    license = License()
    license.set_license("Aspose._3D.lic")
    # ExEnd:ApplyLicenseUsingFile
def UsingStreamObject():
    # ExStart:ApplyLicenseUsingStreamObject
    license = License()
    with open("Aspose._3D.lic", "rb") as myStream:
        license.set_license(myStream)
    # ExEnd:ApplyLicenseUsingStreamObject
def PublicAndPrivateKeys():
    # ExStart:PublicAndPrivateKeys
    # Initialize a Metered license class object
    metered = Metered()
    # Set public and private keys
    metered.set_metered_key("your-public-key", "your-private-key")
    # ExEnd:PublicAndPrivateKeys
