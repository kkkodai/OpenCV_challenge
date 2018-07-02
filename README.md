# Overview
- Contents
    - OpenCV3をインストール → [Install](#install)
    - OpenCV3を使ってみる → [Practice](#practice)
    - **行いたいこと(これが一番重要) → [Task](#task)**
        - 口認識
        - マーカー認識
        - 口のどの位置にマーカーがあるか特定

- OS
    - Mac OSX(El Caption)

# Install
## procedure
1. Xcode
2. pyenv(python3.6.1)
3. autoconf、automake、libtool、CMake (automakeはインストールしなくてもOKかも？)
4. ffmpeg
5. OpenCV

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
## autoconf, automake, libtool, CMake
- automakeはインストールしなくてもOKかも？
```sh
cd ~/Downloads
curl -OL http://ftpmirror.gnu.org/autoconf/autoconf-latest.tar.gz
tar xzf autoconf-latest.tar.gz
cd autoconf-*
./configure --prefix=/usr/local
make && sudo make install

cd ~/Downloads
curl -fL http://ftpmirror.gnu.org/automake/automake-1.15.tar.gz | tar xzf -
cd automake-*
./configure --prefix=/usr/local
make && sudo make install

cd ~/Downloads
curl -fL http://ftpmirror.gnu.org/libtool/libtool-2.4.6.tar.gz | tar xzf -
cd libtool-*
./configure --prefix=/usr/local
make && sudo make install

cd ~/Downloads
curl -OL https://cmake.org/files/v3.8/cmake-3.8.1-Darwin-x86_64.tar.gz
tar xzf cmake-3.8.1-Darwin-x86_64.tar.gz
cd cmame-*
cp CMake.app /Applications/

ln -s "/Applications/CMake.app/Contents/bin/ccmake" /usr/local/bin/ccmake
ln -s "/Applications/CMake.app/Contents/bin/cmake" /usr/local/bin/cmake
ln -s "/Applications/CMake.app/Contents/bin/cmake-gui" /usr/local/bin/cmake-gui
ln -s "/Applications/CMake.app/Contents/bin/cmakexbuild" /usr/local/bin/cmakexbuild
ln -s "/Applications/CMake.app/Contents/bin/cpack" /usr/local/bin/cpack
ln -s "/Applications/CMake.app/Contents/bin/ctest" /usr/local/bin/ctest
```
## FFmpeg
```sh
cd ~/Downloads
curl -LO https://pkg-config.freedesktop.org/releases/pkg-config-0.29.2.tar.gz
tar xf pkg-config-0.29.2.tar.gz
cd pkg-config-0.29.2
./configure --with-internal-glib
make && make install

cd ~/Downloads
curl -LO http://www.tortall.net/projects/yasm/releases/yasm-1.3.0.tar.gz
tar xf yasm-1.3.0.tar.gz
cd yasm-1.3.0
./configure
make && make install

cd ~/Downloads
curl -LO http://www.ffmpegmac.net/resources/ffmpeg-3.3.1.tar.bz2
tar xf ffmpeg-3.3.1.tar.bz2
cd ffmpeg-3.3.1
./configure
make && make install
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

# 動作確認
- 以下のコマンドでerrorを吐かなければOK
```sh
$ python
Python 3.6.1 (default, Mar 30 2017, 09:04:09) 
[GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.42.1)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import cv2
>>> exit()
$ 
```

# Reference
- OpenCV3のインストール方法はこのサイトを参考にしました(神記事)
    - [Macで深層学習の環境をさくっと作る手順 with TensorFlow and OpenCV](https://qiita.com/mix_dvd/items/b49651cf1181a986506c)<br>
    
# Practice
- capture1_face.py
    - Macのwebカメラで顔認識
- capture1_face_eyes.py
    - Macのwebカメラで顔と両目の認識
- capture2.py
    - 画面をぼやけさせる

# Task
- ### capture_mouth.py
    - タスク：口認識を行う
    - 問題点：haarcascade_mcs_mouth.xmlがない<br>
    →　[node-opencv](https://github.com/peterbraden/node-opencv)レポジトリにあったため、使ってみるが全身口だらけになった

- マーカー検出

- 口のどの位置にマーカーがあるか特定

# 方針変更か
- Dlibの方が精度良いとのこと
    - ラズパイに入れられる？