# contracts/asa_contract.py
# Simple Algorand ASA Example using PyTeal

from pyteal import *

def approval_program():
    on_creation = Seq([
        App.globalPut(Bytes("Creator"), Txn.sender()),
        Return(Int(1))
    ])

    on_delete = Return(Txn.sender() == App.globalGet(Bytes("Creator")))

    program = Cond(
        [Txn.application_id() == Int(0), on_creation],
        [Txn.on_completion() == OnComplete.DeleteApplication, on_delete],
    )

    return program

if __name__ == "__main__":
    print(compileTeal(approval_program(), mode=Mode.Application, version=6))
