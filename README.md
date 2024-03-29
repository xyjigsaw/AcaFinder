# AcaFinder (学术访达)

![](https://img.shields.io/badge/Require-Updating-brightgreen.svg)

AcaFinder: Academic Finder for Researchers

The work is part of my Graduate Design.

## Framework
<img src="https://github.com/xyjigsaw/AcaFinder/blob/master/AcaFinder%20Architecture.png?" height = "300" alt="architecture" 
align=center>

Details:

- Data source: [Aminer](https://www.aminer.cn/aminernetwork)
- Profile Extraction and Data Cleaning
- Knowledge Graph Embedding and Fusion
- Storage and Index
- Visualization and Application (like recommendation system)

# Install and Run
unzip static assets
```bash
git clone https://github.com/xyjigsaw/AcaFinder
cd AcaFinder
cd web
unzip static.zip
cd ..
```

Open Neo4j and run AcaFinder Database
```bash
python manage.py runserver
```
or
```bash
python manage.py runserver 0.0.0.0:8000
```


## Preview
![](https://github.com/xyjigsaw/AcaFinder/blob/master/preview2.png)
![](https://github.com/xyjigsaw/AcaFinder/blob/master/preview3.png)
