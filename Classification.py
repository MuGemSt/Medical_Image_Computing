from modelscope.msdatasets import MsDataset
from sklearn.svm import LinearSVC
from datasets import load_dataset
import warnings

warnings.filterwarnings("ignore")


def svm():
    # Load data
    try:
        dataset = load_dataset("MuGemSt/Pima")
    except ConnectionError:
        dataset = MsDataset.load("MuGemSt/Pima", subset_name="default")

    trainset = dataset["train"]
    testset = list(dataset["validation"]) + list(dataset["test"])

    # Preprocess data
    x_train, y_train, x_test, y_test = [], [], [], []

    for item in trainset:
        item_vals = list(item.values())
        x_train.append(item_vals[1:-2])
        y_train.append(item_vals[-1])

    for item in testset:
        item_vals = list(item.values())
        x_test.append(item_vals[1:-2])
        y_test.append(item_vals[-1])

    # Train
    clf = LinearSVC(loss="hinge", random_state=42, max_iter=700000).fit(
        x_train, y_train
    )

    # Test
    print(f"{round(100.0 * clf.score(x_test, y_test), 2)}%")


if __name__ == "__main__":
    svm()