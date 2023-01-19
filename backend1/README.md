# FastAPI導入コマンド
```
pip install fastapi uvicorn
```

# サーバー起動コマンド
```
uvicorn main:app --reload
```
解説：main.pyのFastAPIインスタンスを指定 app=FastAPI()

# 仮想環境 (env) $python -V  3.8.1
    [activate]
        Mac source env/bin/activate
        win env\Scripts\Activate.ps1
    [deactivate]
        deactivate

# 別環境で作業するときはIPアドレスなどを変更して作業する
    CONSTファイル