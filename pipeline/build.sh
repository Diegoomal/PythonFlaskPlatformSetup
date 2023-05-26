
echo "===== bash build ====="

echo "1) Reset environment"

# source pipeline/destroy.sh

echo "2) copiar database"

git clone https://github.com/Diegoomal/ebeer_dataset.git

echo "4) Conda environment"

conda deactivate

conda env create -n project-env -f ./env.yml

conda activate project-env

echo "5) LINT verify with Flak8"

flake8 . --count --statistics

flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

echo "6) Unity test with pytest"

pytest -s

echo "7) Generating documentation"

# pdoc src -o docs

echo "8) Run project"

# python src/main.py

python z/ebeer_training.py

# jupyter notebook notebook.ipynb
# jupyter nbconvert --execute data_augmentation.ipynb