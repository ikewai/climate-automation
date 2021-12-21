FROM ikewai/cat-base

RUN apt update

## OS Dependencies for Python packages ##
ENV DEBIAN_FRONTEND=noninteractive
# - For gdal (version to match python)
RUN apt install -y libgdal-dev=3.0.4+dfsg-1build3

## Python Dependencies for Preliminary Workflow
RUN python3 -m pip install rasterio
RUN python3 -m pip install matplotlib
RUN python3 -m pip install numpy
RUN python3 -m pip install pandas
RUN python3 -m pip install gdal==3.0.4
RUN python3 -m pip install affine
RUN python3 -m pip install pyproj
RUN python3 -m pip install statsmodels
RUN python3 -m pip install scipy
RUN python3 -m pip install scikit-learn