# Image Resize
Resize single image or a set of images stored in directory with super ease.

## Development Enviroment
Python 3.7.4 64-bit

PIL version - 6.1.0

## Packages Required
P(ython) I(maging) L(ibrary)
```
pip install Pillow
```
Rest of the packages are installed by default with Python.

## Usage
> Make sure python is added to enviroment variable path

### In CMD:
```
py pathToFolder/ReduceImageSize.py --help
```

#### If you want to process a single image
```
py pathToFolder/ReduceImageSize.py -i D:/pathToImage -l 250 -b 460
```

#### If you want to process images in directory
This will process all the images in directory.
```
py pathToFolder/ReduceImageSize.py -d D:/pathToFolder -l 250 -b 460
```

#### If you want to maintain the aspect ratio based on height
```
py pathToFolder/ReduceImageSize.py -i D:/pathToImage -l 250 -a True
```

#### Default Values
```
l |    height    | 400  
b |    width     | 400  
a | Aspect Ratio | False
```

### From Developer:
Feel free to use it for any commercial or non-commercial use. 
If you're stuck ping me!
Contact me: abhiishek.srivastava@gmail.com
