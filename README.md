# Features
- Overview
    - Python3でOpenCV3が動くようにする、それと練習

- OS
    - Mac OSX(El Caption)

# Requirement
- Xcode
- autoconf、automake、libtool、CMake (automakeはインストールしなくてもOKかも？)
- pyenv(python3.6.1)
- ffmpeg

# Install
## Xcode
- App Storeを起動してXcodeをインストール
## pyenv
- Referenceではanacondaもインストールしている → [Reference](#reference)

```sh
git clone https://github.com/yyuu/pyenv.git ~/.pyenv

echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc

echo 'if [ -f ~/.bashrc ] ; then' >> ~/.bash_profile
echo '. ~/.bashrc' >> ~/.bash_profile
echo 'fi' >> ~/.bash_profile

source ~/.bashrc

pyenv install 3.6.1
pyenv global 3.6.1
```


## OpenCV
```sh
cd ~/Downloads
git clone https://github.com/Itseez/opencv.git opencv
git clone https://github.com/Itseez/opencv_contrib.git opencv_contrib

cd opencv
mkdir build
cd build
cmake -D CMAKE_BUILD_TYPE=RELEASE \
-D BUILD_SHARED_LIBS=OFF \
-D CMAKE_INSTALL_PREFIX=/usr/local \
-D FFMPEG=ON \
-D PYTHON3_EXECUTABLE=/Users/[username]/.pyenv/versions/anaconda3-4.3.1/bin/python \
-D PYTHON3_INCLUDE_DIR=/Users/[username]/.pyenv/versions/anaconda3-4.3.1/include/python3.6m \
-D PYTHON3_LIBRARY=/Users/[username]/.pyenv/versions/anaconda3-4.3.1/lib/libpython3.6m.dylib \
-D PYTHON3_NUMPY_INCLUDE_DIRS=/Users/[username]/.pyenv/versions/anaconda3-4.3.1/lib/python3.6/site-packages/numpy/core/include \
-D PYTHON3_PACKAGES_PATH=/Users/[username]/.pyenv/versions/anaconda3-4.3.1/lib/python3.6/site-packages \
-D INSTALL_C_EXAMPLES=OFF \
-D INSTALL_PYTHON_EXAMPLES=ON \
-D BUILD_EXAMPLES=ON \
-D BUILD_opencv_python3=ON \
-D OPENCV_EXTRA_MODULES_PATH=~/Downloads/opencv_contrib/modules \
..
make -j4
make install
```

# Reference
- OpenCV3のインストール方法はこのサイトを参考にしました
    - [Macで深層学習の環境をさくっと作る手順 with TensorFlow and OpenCV](https://qiita.com/mix_dvd/items/b49651cf1181a986506c)<br>
    