import os

def get_model_path():
    # import os ...
    # 이 함수 파일의 절대 경로를 받아온다.
    # 절대 경로를 이용해 model.pkl의 경로를 조합
    # 조합된 경로를 리턴 = 끝

    f = __file__
    print(f)
    
    path = os.path.abspath(f)
    dir_name = os.path.dirname(path)
    
    pkl_path = os.path.join(dir_name, "model.pkl")
    
    #home_dir = os.path.expanduser('~')
    #movie_data = pd.read_(f"{home_dir}/code/fishmlserv/src/fishmlserv/model/manager.py")   
    #mp = picle.load(movie_data)


    # 사용 fastapi main.py에서 아래와 같이 사용
    # from fishmlserv.model.manager import get_modle_path
    return pkl_path
