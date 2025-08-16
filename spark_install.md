brew install openjdk@11
brew install apache-spark  

Відкрий конфіг для шелла (залежно від того, що ти юзаєш, наприклад ~/.zshrc або ~/.bash_profile):
    nano ~/.zshrc
Додай туди (якщо ще нема):
    export JAVA_HOME=/opt/homebrew/opt/openjdk@17
    export PATH=$JAVA_HOME/bin:$PATH
Перезавантаж конфіг:
    source ~/.zshrc

Прописати шлях до spark
export SPARK_HOME=/opt/homebrew/Cellar/apache-spark/4.0.0/libexec

В PyCharm Run Config Edit Configuration прописати змінні
SPARK_HOME=/opt/homebrew/Cellar/apache-spark/4.0.0/libexec
JAVA_HOME=/opt/homebrew/opt/openjdk@17