
# シミュレーション自習結果サマリ
## 1.気球上昇下降運動シミュレーション



## 2 ダイナミクスモデル


## 3 システムモデル


## 4 制御モデル






## 5 Environment models(環境モデル)
現在のシミュレーションで採用している環境モデルについて示す.

### 5.1 Isothermal Atmosphere model(等温大気モデル)
大気密度の計算は等温大気モデルを採用しenvironment/atomosphere/isothermal_model.pyにて計算している.

1976 US Standard Atmosphere Table と密度値を比較し，相対誤差が概ね10 [%]以内であることを確認している。

#### Figures
等温大気モデルにおける高度と密度の関係を以下示す.

![density](https://okuma-space.github.io/balloon-simulation/png/isothermal_density.png)

#### Interactive Figures
[graph](https://okuma-space.github.io/balloon-simulation/html/isothermal_density.html)

### 5.2 Layered Temperature Model(分層大気温度モデル)
大気温度の計算は1976 US Standard Atmosphere Tableをベースに以下のように分層化した.
```bash
- 1層(0~12[km])
  - 288.1[K]から216.6[K]までの線形補間
- 2層(12~20[km])
  - 216.6[K]一定
- 3層(20~35[km])
  - 216.6[K]から235[K]までの線形補間
- 4層(35~50[km])
  - 235[K]から270[K]までの線形補間
- 5層 (>50 km)
  - 270[K]一定(将来的にはここも線形補間とする) [issues](https://github.com/okuma-space/balloon-simulation/issues/18)
```

数値計算はenvironment/atomosphere/layered_temperature_model.pyにて計算している.

1976 US Standard Atmosphere Table と温度値を比較し，相対誤差が概ね2.5 [%]以内であることを確認している.

https://www.pdas.com/atmosTable1SI.html

#### Figures
分層大気温度モデルにおける高度と温度の関係を以下示す.

![temperature](https://okuma-space.github.io/balloon-simulation/png/layered_temperature.png)

#### Interactive Figures
[graph](https://okuma-space.github.io/balloon-simulation/html/layered_temperature.html)


## Appendix. 過去versionの検証ログ(保存/振り返り用)
### version0.0
version0.0としてまずは等速直線運動モデルを実装した.

等速直線運動でaltitudeだけ一定速度で上昇していく事が確認できた.

[Repository](https://github.com/okuma-space/rocket-simulation/tree/v0.0)

[PR](https://github.com/okuma-space/rocket-simulation/pull/1)

#### Figures
![pos_vel](https://okuma-space.github.io/rocket-simulation/png/rocket_altitude_history_0.0.png)

#### Interactive Figures
[pos_vel](https://okuma-space.github.io/rocket-simulation/html/rocket_altitude_history_0.0.html)