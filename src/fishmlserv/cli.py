import pickle
import typer
from typer.colors import RED
from fishmlserv.model.manager import get_model_path

app = typer.Typer()

@app.command()
def prediction(
    l: float = typer.Option(..., "--length", "-l", help="Length of the fish"),
    w: float = typer.Option(..., "--weight", "-w", help="Weight of the fish")
):
    """
    Predict the type of fish based on its length and weight.
    """
    # 모델 로드
    with open(get_model_path(), "rb") as f:
        fish_model = pickle.load(f)

    # 예측 수행
    result = fish_model.predict([[l, w]])[0]

    # 예측 결과 출력
    if result == 1:
        typer.secho("도미")
    else:
        typer.secho("빙어")

if __name__ == "__main__":
    app()
