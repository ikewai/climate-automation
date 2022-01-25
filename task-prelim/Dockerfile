FROM ikewai/cat-base

# Important note: This base container relies on the concept that all
# preliminary workflows don't have version conflicts with their dependencies.
# If a conflict occurs in the future, it will be necessary to either move the installations
# to specific base containers for each workflow, or to use uninstall/install overrides in
# their specific dockerfiles.

RUN apt update
ENV DEBIAN_FRONTEND=noninteractive

## OS Dependencies for Python packages ##
# - For gdal (version to match python)
RUN apt install -y libgdal-dev=3.0.4+dfsg-1build3

RUN apt install -y r-base libxml2-dev libssl-dev curl libcurl4-openssl-dev

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
RUN python3 -m pip install tiffile
RUN python3 -m pip install agavepy
RUN python3 -m pip install python-dotenv
RUN python3 -m pip install pathlib
RUN python3 -m pip install xarray
RUN R -e 'install.packages(c("ggplot2"))'
RUN R -e 'install.packages(c("xts"))'
RUN R -e 'install.packages(c("RNRCS"))'
RUN R -e 'install.packages(c("metScanR"))'
RUN R -e 'install.packages(c("lubridate"))'
RUN R -e 'install.packages(c("plyr"))'
RUN R -e 'install.packages(c("reshape2"))'
RUN R -e 'install.packages(c("raster"))'
RUN R -e 'install.packages(c("sp"))'
RUN R -e 'install.packages(c("doParallel"))'
RUN R -e 'install.packages(c("foreach"))'
RUN R -e 'install.packages(c("fitdistrplus"))'
RUN R -e 'install.packages(c("tidyr"))'
RUN R -e 'install.packages(c("e1071"))'
RUN R -e 'install.packages(c("Metrics"))'
RUN R -e 'install.packages(c("rgdal"))'
RUN R -e 'install.packages(c("geosphere"))'
RUN R -e 'install.packages(c("data.table"))'
RUN R -e 'install.packages(c("randomForest"))'
RUN R -e 'install.packages(c("caret"))'
RUN R -e 'install.packages(c("dplyr"))'

WORKDIR /sync

RUN wget https://raw.githubusercontent.com/ikewai/data-uploader/main/upload.py

COPY upload_auth_injector.py .