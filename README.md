## Simple-Behavioral-Discounting-Model

This project models how people value future rewards less than immediate ones — a behavior known as **time discounting**. It helps explain why we procrastinate or choose quick pleasures over long-term benefits. For people with **ADHD**, this effect can be stronger, making it harder to stay focused on delayed goals. The model sums the expected value of an action at different future times, weighted by how important that time feels. It helps compare actions and design ways to motivate better choices and reduce procrastination, especially for those with attention challenges.

### 1. Key Concept

The model computes a weighted sum of future subjective values, the total behavioral utility, to evaluate how appealing a behavior is from the present perspective.
The total behavioral utility is given by:

$$U = \int_{t_0}^{\infty} W(t) \cdot V(t) \, dt$$

- **U** is the total utility accumulated from the present time $$t_0$$ onward.
- **W(t)**: Discount weight function  
  Describes how much a person values events at future time $$t$$.
- **V(t)**: Expected value function  
  Represents the subjective utility ("pleasure") from a behavior at time $$t$$.

---

### 2. Model Components

We use classic function forms for interpretability.

#### 2.1 Discount Weight Function $$W(t)$$

Using **hyperbolic discounting**, commonly found in behavioral economics:

$$W(t) = \frac{1}{1 + k t}$$

Where:

- $$k > 0$$: discount rate (larger means more short-sightedness)

> _Alternative (simpler but less realistic):_  
> Exponential discounting:  $$W(t) = e^{-r t}$$

#### 2.2 Expected Value Function $$V(t)$$

Two common choices:

- Constant value:  $$V(t) = V_0$$

- Exponential decay:  $$V(t) = V_0 \cdot e^{-\lambda t}$$

---

### 3. Model Example

#### 3.1 Constant V(t) - Divergence
Assume:

- $$V(t) = V_0$$
- $$W(t) = \frac{1}{1 + k t}$$
- $$t_0 = 0$$

Then:

$$U = \int_0^{\infty} V_0 \cdot \frac{1}{1 + k t} \, dt = V_0 \cdot \int_0^{\infty} \frac{1}{1 + k t} \, dt$$

Substitute:  
Let $$u = 1 + k t \Rightarrow du = k dt$$

$$U = \frac{V_0}{k} \int_1^{\infty} \frac{1}{u} \, du = \frac{V_0}{k} [\ln u]_1^{\infty}$$

This diverges because:

$$\ln(\infty) = \infty$$

Total utility becomes infinite if future value is constant and discounting is too slow.  
This reflects the **“procrastination trap”** — future rewards are always tempting but never acted upon.

#### 3.2 Value with Decay - Convergence

Use an exponentially decreasing value function:

$$V(t) = V_0 \cdot e^{-\lambda t}$$

Then:

$$U = \int_0^{\infty} \frac{V_0 \cdot e^{-\lambda t}}{1 + k t} \, dt$$

This is usually convergent (though lacks a closed-form), and can be approximated numerically.

---

### 4. Final Model Summary

$$U = \int_{t_0}^{\infty} W(t) \cdot V(t) \, dt = \int_0^{\infty} \frac{V_0 \cdot e^{-\lambda t}}{1 + k t} \, dt$$

- `V(t)`: The **subjective value** (e.g., anticipated happiness or positive outcome) that the behavior brings at future time `t`
- `W(t)`: The **discount weight function**, reflecting how much importance we place on outcomes at time `t`  
  (usually, **closer** means more important; **farther** means less important)
- $$k$$: how short-sighted the decision-maker is  
- $$\lambda$$: how fast value decays over time  
- $$V_0$$: the behavior’s base utility

This is a **1-to-1 behavioral model** designed to capture **how people evaluate the utility of a single behavior over time**.

It specifically describes:

- A particular behavior (e.g., _"study for one hour each day"_, _"start a project"_, _"exercise today"_)
- The **expected utility this behavior generates over time**

This integral captures the **weighted sum of future benefits**, discounted by how we perceive time.

---

### 5. Real Life Example: Behavior A vs Behavior B

| Behavior | Description         | V(t) Profile |
|----------|---------------------|--------------------|
| A        | Start exercising    | Painful at first, but increasing value over time (better health, physique) |
| B        | Scroll short videos | Instant pleasure, but low or even negative value over time (regret, wasted time) |

By comparing `U_A` and `U_B`, we can infer which action we'd rationally prefer — if we were to evaluate based on total discounted utility.

---

### 6. Scaling to Multiple Behaviors

To compare **more than two behaviors**, we upgrade the model to **optimal behavior selection**:

$$ a^* = \arg\max_{a \in A} \int_0^\infty W(t) \cdot V_a(t) \, dt $$

Where:

- $$A$$ is the set of all possible behaviors (e.g. exercise, study, play games, sleep)
- $$a*$$ is the behavior with the highest expected discounted utility

---

### 7. Enhancing Behavioral Utility via Scaling and Shifting $$V(t)$$

The core insight behind applying scaling and shifting transformations to the value function $$V(t)$$ lies in how humans perceive rewards over time and how the model mathematically discounts future outcomes.
By applying **scaling and shifting transformations** to the value function $$V(t)$$, we can turn a behavior that is originally *not attractive enough* into one that people want to do immediately — i.e., it gains a **huge boost in utility(U)** within the model.


#### 7.1 Method 1: Increase the immediate value $$V(0)$$

This is the most direct method. If a behavior's reward only happens in the future (e.g., "do well on an exam"), it’s hard to motivate immediate action.

**Real-world examples:** 
- Add an immediate reward — like earning stars after checking in, or enjoying a delicious smoothie right after exercising — effectively increasing $$V(0)$$.

**Mathematically:**

$$V(t) \to V(t) + \delta(t) \cdot R$$

where $$\delta(t)$$ is the Dirac delta function (an instantaneous reward pulse at $$t=0$$).

See the accompanying Python script [`1_immediate_reward.py`](./1_immediate_reward.py) for the following dynamic visualization of how adding an immediate reward changes the utility curve over time.

![immediate_reward_utility](https://github.com/user-attachments/assets/4b0933af-1f70-47c6-8c48-5cb7dde58044)

**Effect on Utility Curve:**
- Creates a sharp **spike at \( t = 0 \)** (where discounting is minimal).
- Generates a **significant immediate boost in total utility**.
- Very efficient for short-sighted individuals (high discount rate \( k \)).

**Behavioral Insight:**
- **Immediate gratification** is highly motivating.
- Even small rewards now can outweigh larger rewards later.
- Especially helpful for individuals with **ADHD** who struggle with delayed outcomes.

**Limitation:**
- Effect may be short-lived without future rewards.
- Not sufficient for sustaining long-term motivation on its own.

---

#### 7.2 Method 2: Time compression or bringing future rewards closer

Some behaviors are hard to start because their rewards come too far in the future (e.g., exam results, weight loss, long-term savings). By mentally or structurally “previewing” these rewards earlier, we can make the behavior feel more worthwhile now.

**Real-world examples:**
- Getting instant positive AI feedback immediately after studying (even though the exam is later)
- Seeing VO2max improvement data after running (before the visible body changes)

**Mathematically:**

Suppose the original function is: 

$$V(t) = V_0 e^{-\lambda t}$$

We can transform it as:

$$V'(t) = V_0 e^{-\lambda (t - \tau)}, \quad t \geq \tau$$

Meaning: rewards that originally appear at day 10 now start previewing at day 3.

See the Python script [`2_left_shift_reward.py`](./2-left_shift_reward.py) for the following animated visualization of how left-shifting the value function boosts near-term utility.

![left_shift_utility](https://github.com/user-attachments/assets/b5bf57b8-f6aa-48ea-8f3d-b6fa56afe244)

**Effect on Utility Curve:**
- Moves the value curve **closer to the present**, increasing early utility.
- Makes more of the value function fall under the high-weight region of \( W(t) \).
- Results in a **smooth rise in utility** over time.

**Behavioral Insight:**
- Previewing success or progress helps make long-term goals feel real now.
- Effective for **learning, fitness, or project tracking**.
- Reduces frustration for ADHD individuals by **bridging feedback delays**.

**Limitation:**
- Requires mechanisms for early feedback or visualization (e.g., apps, simulations).
- Not all outcomes can be meaningfully previewed early.



---
#### 7.3 Method 3: Compress the value function (increase compactness)

Rather than waiting for a distant reward to arrive, we can compress the timeline so that value is delivered in smaller, quicker chunks. This makes future rewards more immediate and keeps motivation alive.

**Real-world examples:**

- A week-long task broken into daily smaller tasks with daily feedback
- This compression boosts motivation by making rewards more immediate

**Mathematically:**

Shift the function left by compressing time:

$$V'(t) = V(\alpha t), \quad 0 < \alpha < 1$$

This releases future value earlier, capturing it before discounting reduces its impact.

See the Python script [`3_time_compression.py`](./3_time_compression.py) for the following animated visualization of how compressing time increases the perceived utility of future rewards.


![time_compression_utility](https://github.com/user-attachments/assets/09bb0a7b-9f10-4850-8778-45cf72f6d0e2)


**Effect on Utility Curve:**
- The value curve becomes **more compact**, delivering value earlier.
- Shifts utility density to regions where discounting is weaker.
- Produces **more value sooner**, though more gradually than Method 1.

**Behavioral Insight:**
- Perfect for **task breakdown and micro-goal setting**.
- Encourages momentum through frequent **small wins**.
- Helps individuals with ADHD stay engaged by reducing time to reward.

**Limitation:**
- Requires task restructuring; can't compress everything (e.g., long-term biological outcomes).
- Less dramatic boost than Method 1 but more sustainable.

---

#### 7.4 Why this yields huge gains:

The discount function $$\frac{1}{1 + k t}$$ is very steep near $$t \to 0$$.  
Moving value slightly closer to the present greatly increases the total utility $$U$$.

Even slightly bringing forward feedback can motivate someone to start a behavior they would otherwise avoid.

#### 7.5 Summary (Behavior Design Perspective)

We can greatly boost the *psychological utility* of a behavior by applying these interventions on $$V(t)$$:

| Operation        | Mathematical Transformation          | Behavioral Explanation          |
|------------------|------------------------------------|--------------------------------|
| Inject Immediate Reward | $$V(t) + \delta(t) \cdot R$$     | Rewards, encouragement systems |
| Time Compression | $$V(\alpha t)$$                   | Task breakdown, short-term goals |
| Left Shift       | $$V(t - \tau)$$                   | Prepaid rewards, visual progress |
| Amplify Value    | $$c \cdot V(t)$$                  | Increase importance, sense of achievement |



