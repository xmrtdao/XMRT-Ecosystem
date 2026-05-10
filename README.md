# XMRT-Ecosystem - Fully Autonomous DAO

[![HF Space](https://img.shields.io/badge/🤗%20Hugging%20Face-Space-blue)](https://huggingface.co/spaces/XMRTDAO/XMRT-Ecosystem)
[![GitHub](https://img.shields.io/badge/GitHub-Repo-black)](https://github.com/xmrtdao/XMRT-Ecosystem)

Welcome to the XMRT-Ecosystem repository! This repository houses the various decentralized applications (dApps) and core components that form the XMRTNET ecosystem, powered by **Autonomous ElizaOS** - a fully autonomous AI agent system.

## 🤖 Autonomous ElizaOS

ElizaOS is the brain of the XMRT DAO. It:
- Proposes governance actions autonomously
- Manages treasury rebalancing strategies
- Coordinates mesh network node deployment
- Interfaces with human executives for approval

## 📜 Smart Contracts

| Contract | Purpose | Status |
|----------|---------|--------|
| `XMRT.sol` | ERC-20 token with governance | ✅ Implemented |
| `DAO_Treasury.sol` | Multi-sig treasury management | ✅ Implemented |
| `AutonomousTreasury.sol` | AI-managed yield strategies | ✅ Implemented |
| `Governance.sol` | Proposal/vote/tally logic | ✅ Implemented |
| `AutonomousDAO.sol` | Agent registry + permissions | ✅ Implemented |
| `Vault.sol` | Asset custody | ✅ Implemented |
| `XMRTCrossChain.sol` | Cross-chain bridging | ✅ Implemented |
| `XMRTLayerZeroOFT.sol` | LayerZero OFT standard | ✅ Implemented |

### Key Functions

#### AutonomousTreasury.sol
- `_executeAssetRebalance(address, uint256, uint256)` — Rebalances asset allocation based on deviation from target
- `_getPendingYield(address)` — Calculates simple interest: `principal * APY * time / (365 * BASIS_POINTS)`
- `_harvestAssetYield(address, uint256)` — Records yield generation

## 🗂️ Project Structure

```
XMRT-Ecosystem/
├── contracts/          Solidity smart contracts
├── backend/            Python Flask services
│   ├── ai-automation-service/
│   ├── cross-chain-service/
│   └── xmrt-dao-backend/
├── frontend/           React/Next.js interface
└── scripts/            Deployment and utility scripts
```

## 🚀 Deployment

```bash
# Compile contracts
forge build

# Run tests
forge test

# Deploy to testnet
forge script scripts/Deploy.s.sol --rpc-url $RPC_URL --broadcast
```

## 🔗 Related Repos

- [suite](https://github.com/xmrtdao/suite) — Supabase edge functions + AI chat
- [xmrtnet](https://github.com/xmrtdao/xmrtnet) — Flask backend services
- [cashdapp](https://github.com/xmrtdao/cashdapp) — Mobile payment interface
- [zero-claw](https://github.com/xmrtdao/zero-claw) — ZK governance layer (AMD Hackathon 2026)

## 🛡️ Security

All contracts have been audited for:
- Reentrancy protection
- Access control (OpenZeppelin AccessControl)
- Integer overflow checks (Solidity ^0.8.19)
- Yield calculation accuracy

See `SECURITY.md` for detailed policy.
