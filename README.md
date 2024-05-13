<h1>使用方式:</h1>
<ol>
    <li>clone git 專案</li>
    <li>在專案中啟動 venv</li>
    <li>pip install -r requirements.txt</li>
    <li>建立.env檔案</li>
    <li>
        複製以下項目到.env中
        <p>
            FLASK_ENV = "development"<br/>
            FLASK_DEBUG = 1<br/>
            FLASK_RUN_PORT = 8000<br/>
            SQLALCHEMY_DATABASE_URI =<br/>
        <p> 
    </li>
    <li>依自己需求輸入SQLALCHEMY_DATABASE_URI</li>
    <li>引入根目錄中的db.sql到自己的mysql browser(ex: mysql workbench、mariadb(Heidi DB))</li>
</ol>