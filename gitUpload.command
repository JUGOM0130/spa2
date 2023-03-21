#!/bin/bash

git add .
git commit -m "bachAddMac"
git push

#スクリプトは必ずルートディレクトリで開始されるため
#下記コマンドで.commandファイルのあるフォルダへ移動できる
cd `dirname $0`

cd frontend
git add .
git commit -m "bachAddMac"
git push

#ディレクトリ移動
cd `dirname $0`

cd backend
git add .
git commit -m "bachAddMac"
git push
