from fastapi.testclient import TestClient

from app.api.dependencies import get_current_user
from app.models.aluno import Aluno
from app.models.enums import MovementType
from app.models.usuario import UsuarioSistema
from app.services.qr_crypto_service import generate_qr_token


def override_get_current_user():
    return UsuarioSistema(
        id=1,
        nome="Operador Test",
        login="op@test.com",
        perfil="PORTARIA",
        status=True,
    )


def test_scan_qr_code_success(client: TestClient, db_session):
    # Setup test data
    aluno = db_session.query(Aluno).filter(Aluno.id == 1).first()
    if not aluno:
        aluno = Aluno(
            id=1,
            matricula="TEST1234",
            nome_completo="Test Student",
            curso="TI",
            qr_code_hash="qr",
        )
        db_session.add(aluno)

    operador = db_session.query(UsuarioSistema).filter(UsuarioSistema.id == 1).first()
    if not operador:
        operador = UsuarioSistema(
            id=1,
            nome="Operador Test",
            login="op@test.com",
            perfil="PORTARIA",
        )
        db_session.add(operador)

    db_session.commit()

    # We generate a valid JWT for Aluno 1
    token = generate_qr_token(aluno_id=1)

    client.app.dependency_overrides[get_current_user] = override_get_current_user

    response = client.post(
        "/api/v1/movimentacao/scan", json={"qr_code_hash": token}
    )

    client.app.dependency_overrides.clear()

    assert response.status_code == 200
    data = response.json()
    assert data["status"] is True
    assert "student_name" in data
    # By default, after seed, they have 2 movements (ENTRADA, SAIDA).
    # The next should be ENTRADA.
    assert data["movement_type"] in [
        MovementType.ENTRADA.value,
        MovementType.SAIDA.value,
    ]


def test_scan_qr_code_invalid_token(client: TestClient):
    client.app.dependency_overrides[get_current_user] = override_get_current_user
    response = client.post(
        "/api/v1/movimentacao/scan",
        json={"qr_code_hash": "invalid-token"},
    )
    client.app.dependency_overrides.clear()

    assert response.status_code == 401
    assert response.json()["detail"] == "Forged or invalid QR Code."


def test_scan_qr_code_student_not_found(client: TestClient):
    # Generates a valid token for a non-existent student ID (9999)
    token = generate_qr_token(aluno_id=9999)

    client.app.dependency_overrides[get_current_user] = override_get_current_user
    response = client.post(
        "/api/v1/movimentacao/scan", json={"qr_code_hash": token}
    )
    client.app.dependency_overrides.clear()

    assert response.status_code == 404
    assert response.json()["detail"] == "Aluno não encontrado."
