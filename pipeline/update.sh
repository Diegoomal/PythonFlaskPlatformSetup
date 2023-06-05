
echo "===== bash update ====="

echo "1) Reset environment"

# source pipeline/destroy.sh

echo "2) Conda environment"

conda deactivate

conda env update -n project-env -f ./env.yml

conda activate project-env

echo "3) LINT verify with Flak8"

flake8 . --count --statistics

flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

echo "4) Generating documentation"

# pdoc src -o docs

echo "5) Run project"

python src/main.py

echo "6) Unity test with pytest"

pytest -s