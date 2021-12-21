# This container has R packages to fulfill dependency requirements of ALL rainfall aggregation tasks.
# It should be used as the base for any rainfall aggregation task.
# Build time (workstation): 25-35 minutes

FROM ikewai/climate-automation-task-base

# Refresh OS package catalog.
RUN apt update

## OS dependencies for R packages ##
# Workaround for r-base install, which normally requires user input to finish.
ENV DEBIAN_FRONTEND=noninteractive
# Install OS packages:
# - for R, RNRCS, openssl, RCurl, and RGdal respectively.
RUN apt install -y r-base
RUN apt install -y libxml2-dev 
RUN apt install -y libssl-dev 
RUN apt install -y curl libcurl4-openssl-dev 
RUN apt install -y libgdal-dev

# Install R packages:
# - for HADS and NWS collection.
RUN R -e 'install.packages(c("ggplot2","xts","RNRCS","metScanR","lubridate","plyr"))'
# - for QAQC computation.
RUN R -e 'install.packages(c("reshape2","raster","sp","doParallel","foreach","fitdistrplus","tidyr","e1071","Metrics","rgdal","geosphere","data.table","randomForest", "caret", "dplyr"))'