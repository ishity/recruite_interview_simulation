![download](https://github.com/user-attachments/assets/6e368484-a8b1-4965-b7c7-3cdb77fb6a44)

## アプリ起動手順
### 仮想環境の作成
```
conda create -n [仮想環境名]
conda activate [仮想環境名]
```
### パッケージのインストール
```
pip install streamlit
```
### ビルド
```
streamlit run app.py
```
## ビルド時の注意
- .envにgptのAPIkeyを下記のように入れるのを忘れないでください
```
export OPENAI_API_KEY='~~'
```
