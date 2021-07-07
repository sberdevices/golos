# build container

export CURRENT_DIR=$PWD

docker build -t golos_image .


#run conatiner 
# requrements (requires 
docker run --gpus all  \
    -v /$CURRENT_DIR/..:/workspace/golos  \
    -it  \
    --shm-size=8g \
    --ulimit memlock=-1 --ulimit \
    stack=67108864 golos_image  
