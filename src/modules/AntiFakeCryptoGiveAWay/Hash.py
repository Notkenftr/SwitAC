async def Hash() -> list:
    import os
    import imagehash
    from PIL import Image
    from ...utils import PathManager


    HashResult = []
    scam_samples_path = os.path.join(PathManager.getRoot(),'assets','scam_samples')




    for sample in os.listdir(scam_samples_path):
        try:
            image = Image.open(os.path.join(scam_samples_path, sample))
            HashResult.append(imagehash.phash(image))
        except Exception as e:
            print(e)

    return HashResult