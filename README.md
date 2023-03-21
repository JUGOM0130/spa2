# mac環境構築

## macエイリアスでpythonコマンドを使用できるようにする
* windowsだとpythonコマンドが ```python```
* macだとpythonコマンドが```python3```
    macにはpython2がデフォルトで入っているから

0. 前提：python3のPATHが通っていること
1.  ```bash
    cd $HOME
    nano .bashrc
    ```

2. エディターで.bashrcを開いたら下記を追記

3. ```
    alias python="python3"
    ```
4. 保存してエディタを終了後下記コマンド実行
5. ```
    nano .bash_profile
    ```
6. 一番下に下記コマンド追記
7. ```
    source ~/.bashrc
    ```
8. エディタを終了して下記コマンド実施
9. ```bash
    source ~/.bash_profile #再読み込みするらしい
    ```
