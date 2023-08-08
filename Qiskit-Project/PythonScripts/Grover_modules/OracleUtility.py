from General_modules import ProtocolManager as pm

def ApplyOracleAlice(backend, qc, alice):
    pm.ApplySingleProtocol(backend, qc, alice, 1)