from deepface import DeepFace
import json


def face_verify(img_1, img_2):
    try:
        result_dict = DeepFace.verify(img1_path=img_1, img2_path=img_2)

        with open('result.json', 'w') as file:
            json.dump(result_dict, file, indent=4, ensure_ascii=False)
        return result_dict
    except Exception as _ex:
        return _ex


def face_recogn():
    try:
        result = DeepFace.find(img_path='12.jpg', db_path='darya')
        result= result.values.tolist()
        return result
    except Exception as _ex:
        return _ex

def face_analyze():
    try:
        result_dict = DeepFace.analyze(img_path= '12.jpg', actions= ['age', 'gender', 'race', 'emotion'])

        with open('face.anakyze.json', 'w') as file:
            json.dump(result_dict, file, indent=4, ensure_ascii=False)
        print(f'[+] Age:{result_dict.get("age)")}')

    except Exception as _ex:
        return _ex


def main():
    print(face_verify(img_1='12.jpg', img_2='13.jpg'))
    print(face_recogn())



if __name__ == 'main':
    main()