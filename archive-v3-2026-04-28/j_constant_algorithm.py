python
import numpy as np
from scipy.special import ellipe
from mpmath import mp, zeta, zetazero
import csv

# =============================================
# 1. 高精度设置与常数定义
# =============================================
mp.dps = 50 # 50 位十进制精度，应对高位零点
gamma = 0.57721566490153286061
J_theory = gamma / (2 * np.pi) # ≈ 0.0918667263

# =============================================
# 2. 椭圆几何计算函数
# =============================================
def compute_b(a, J_target, tol=1e-14, max_iter=100):
    """给定 a = t，求解 b 使得 J(a,b) = J_target"""
    b_low, b_high = 0.0, a
    for _ in range(max_iter):
        b = (b_low + b_high) / 2
        e_sq = 1 - (b**2) / (a**2)
        if e_sq <= 0 or e_sq >= 1:
            b_low = b if e_sq <= 0 else b_low
            b_high = b if e_sq >= 1 else b_high
            continue
        e = np.sqrt(e_sq)
        C = 4 * a * ellipe(e)
        J_calc = (2 * np.pi * (a - b) - C) / 2
        if abs(J_calc - J_target) < tol:
            return b, C, J_calc
        elif J_calc > J_target:
            b_low = b
        else:
            b_high = b
    return b, C, J_calc

def compute_U(a, b, C):
    """计算几何量 U(t) = 2π(a-b) - C"""
    return 2 * np.pi * (a - b) - C

# =============================================
# 3. 耦合判别函数 Ψ(t)
# =============================================
def Psi(t):
    """计算耦合判别函数 Ψ(t)"""
    a = t
    b, C, _ = compute_b(a, J_theory)
    U = compute_U(a, b, C)
    zeta_val = abs(zeta(0.5 + 1j * t))
    zeta_mod_sq = float(zeta_val)**2
    U_term = (U - 2 * J_theory) / (2 * np.pi)
    U_term_sq = U_term**2
    Psi_val = zeta_mod_sq + U_term_sq
    return Psi_val, zeta_mod_sq, U_term_sq, b, C, U

# =============================================
# 4. 批量验证函数
# =============================================
def validate_zeros(zero_indices):
    """验证指定序号的零点列表"""
    results = []
    for idx in zero_indices:
        t = float(zetazero(idx).imag)
        Psi_val, zeta_sq, U_sq, b, C, U = Psi(t)
        results.append({
            'index': idx, 't': t, 'Psi': Psi_val,
            '|ζ|²': zeta_sq, '((U-2J)/(2π))²': U_sq,
            'b': b, 'U': U
        })
    return results

# =============================================
# 5. 主执行区
# =============================================
if __name__ == "__main__":
    zero_indices = list(range(1, 101))
    results = validate_zeros(zero_indices)
    psi_values = [r['Psi'] for r in results]
    print(f"验证完成。Psi 最大值: {max(psi_values):.2e}, 最小值: {min(psi_values):.2e}")

