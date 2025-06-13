# Módulo: test_segura_dados.py

import unittest
import segura_dados as sd

class TestSeguraDados(unittest.TestCase):

    def setUp(self):
        sd.usuarios.clear()  # Limpa dados antes de cada teste

    def test_validar_email(self):
        self.assertTrue(sd.validar_email("teste@email.com"))
        self.assertFalse(sd.validar_email("email_invalido"))

    def test_validar_cpf(self):
        self.assertTrue(sd.validar_cpf("12345678901"))
        self.assertFalse(sd.validar_cpf("12345"))

    def test_cadastro_usuario_valido(self):
        msg = sd.cadastrar_usuario("João", "joao@email.com", "12345678901", "11999999999")
        self.assertEqual(msg, "Usuário cadastrado")
        self.assertIn("joao@email.com", sd.usuarios)

    def test_cadastro_usuario_com_email_invalido(self):
        msg = sd.cadastrar_usuario("Maria", "mariaemail.com", "12345678901", "11988888888")
        self.assertEqual(msg, "Email inválido")

    def test_cadastro_usuario_com_cpf_invalido(self):
        msg = sd.cadastrar_usuario("Lucas", "lucas@email.com", "123", "11977777777")
        self.assertEqual(msg, "CPF inválido")

    def test_buscar_usuario_existente(self):
        sd.cadastrar_usuario("Ana", "ana@email.com", "12345678901", "11966666666")
        usuario = sd.buscar_usuario("ana@email.com")
        self.assertIsNotNone(usuario)
        self.assertEqual(usuario["nome"], "Ana")

    def test_atualizar_usuario(self):
        sd.cadastrar_usuario("Carlos", "carlos@email.com", "12345678901", "11955555555")
        msg = sd.atualizar_usuario("carlos@email.com", "Carlos Silva", "11900000000")
        self.assertEqual(msg, "Dados atualizados")
        self.assertEqual(sd.usuarios["carlos@email.com"]["nome"], "Carlos Silva")

    def test_excluir_usuario(self):
        sd.cadastrar_usuario("Julia", "julia@email.com", "12345678901", "11944444444")
        msg = sd.excluir_usuario("julia@email.com")
        self.assertEqual(msg, "Usuário removido")
        self.assertNotIn("julia@email.com", sd.usuarios)

if __name__ == '__main__':
    unittest.main()