import importlib
from types import ModuleType


def load_package(name: str) -> ModuleType | None:
    try:
        return importlib.import_module(name)
    except ImportError:
        return None


pd = load_package("pandas")
np = load_package("numpy")
plt = load_package("matplotlib.pyplot")
matplotlib = load_package("matplotlib")


def check(pd: ModuleType | None, np: ModuleType | None,
          plt: ModuleType | None, matplotlib: ModuleType | None) -> bool:
    if pd:
        print(f"[OK] pandas ({pd.__version__}) - Data manipulation ready")
    else:
        print("[MISSING] pandas")
    if np:
        print(f"[OK] numpy ({np.__version__}) - Numerical Computation ready")
    else:
        print("[MISSING] numpy")
    if plt and matplotlib:
        print(f"[OK] matplotlib ({matplotlib.__version__})"
              f" - Visualization ready")
    else:
        print("[MISSING] matplotlib")
    if pd and np and plt and matplotlib:
        return True
    else:
        print("\nTo install dependencies:")
        print("With pip:    pip install -r requirements.txt")
        print("With poetry: poetry install")
        return False


def analys(pd: ModuleType, np: ModuleType) -> object:
    print("\nAnalyzing Matrix data...")
    print("Processing 1000 data points...")
    data = np.random.randn(1000)
    df = pd.DataFrame(data, columns=["Matrix_data"])
    return df


def visualize(plt: ModuleType, df: object) -> None:
    plt.figure(figsize=(10, 6))
    plt.plot(df)
    plt.savefig("matrix_analysis.png")
    plt.close()


if __name__ == "__main__":
    print("\nLOADING STATUS: Loading programs...")
    print("\nChecking dependencies:")
    if check(pd, np, plt, matplotlib) and pd and np and plt:
        df = analys(pd, np)
        print("Generating visualization...")
        visualize(plt, df)
        print("\nAnalysis complete!")
        print("Results saved to: matrix_analysis.png")
