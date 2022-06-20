FROM ikewai/task

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
RUN R -e 'install.packages("ggplot2")'
RUN R -e 'install.packages("xts")'
RUN R -e 'install.packages("metScanR")'
RUN R -e 'install.packages("lubridate")'
RUN R -e 'install.packages("plyr")'
RUN R -e 'install.packages("reshape2")'
RUN R -e 'install.packages("raster")'
RUN R -e 'install.packages("sp")'
RUN R -e 'install.packages("doParallel")'
RUN R -e 'install.packages("foreach")'
RUN R -e 'install.packages("fitdistrplus")'
RUN R -e 'install.packages("tidyr")'
RUN R -e 'install.packages("e1071")'
RUN R -e 'install.packages("Metrics")'
RUN R -e 'install.packages("rgdal")'
RUN R -e 'install.packages("geosphere")'
RUN R -e 'install.packages("data.table")'
RUN R -e 'install.packages("https://cran.r-project.org/src/contrib/Archive/randomForest/randomForest_4.6-14.tar.gz", repos=NULL, type="source")'
RUN R -e 'install.packages("caret")'
RUN R -e 'install.packages("dplyr")'
RUN R -e 'install.packages("matrixStats")'

WORKDIR /sync

RUN wget https://raw.githubusercontent.com/ikewai/data-uploader/main/upload.py

COPY upload_auth_injector.py .
COPY update_date_string_in_config.py .