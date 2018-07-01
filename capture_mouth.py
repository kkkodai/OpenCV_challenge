# coding: utf-8

import cv2 

if __name__ == "__main__":
    
    # 内蔵カメラを起動
    cap = cv2.VideoCapture(0)

    # OpenCVに用意されている顔認識するためのxmlファイルのパス
    cascade_path = "/usr/local/share/OpenCV/haarcascades/haarcascade_mcs_mouth.xml"
    # カスケード分類器の特徴量を取得する
    cascade = cv2.CascadeClassifier(cascade_path)
    
    # 顔に表示される枠の色を指定（白色）
    color = (255,255,255)

    while True:
    
        # 内蔵カメラから読み込んだキャプチャデータを取得
        ret, frame = cap.read()
        facerect = cascade.detectMultiScale(frame, scaleFactor=1.2, minNeighbors=2, minSize=(10,10))
        if len(facerect) > 0:
            for rect in facerect:
                cv2.rectangle(frame, tuple(rect[0:2]), tuple(rect[0:2]+rect[2:4]), color, thickness=2)
        cv2.imshow("frame", frame)

        # ESCキーを押すとループ終了
        key = cv2.waitKey(10)
        if key == 27:
            break

    # 内蔵カメラを終了
    cap.release()
    cv2.destroyAllWindows()