# Core
## gym.Env
###  `gym.Env.step(self, action: ActType) → Tuple[ObsType, float, bool, bool, dict]`

运行环境的一个`time-step`。

当`episode`结束时，需要手动调用 `reset()` 来重置此环境的状态。
接受一个`action`并返回一个元组（`observaion`、`reward`、`terminated`、`truncated`、`info`）。

**参数**:
    
- **action**(*ActType*) - `agent`执行的`action`

**返回值**:
- **observation**(*object*) - 这是环境的 `observation_space` 的一个元素。例如，这可能是一个包含某些对象的位置和速度的 numpy 数组。
- **reward**(*float*) - 采取`action`而返回的`reward`。
- **terminated**(*bool*) - 是否达到了终端状态（如任务的马尔可夫决策过程中所定义）。在这种情况下，进一步的调用 `step()` 可能会返回未定义的结果。
- **truncated**(*bool*)- 是否满足马尔科夫决策过程范围之外的截断条件。通常是时间限制，但也可用于表示`agent`物理上越界。可用于在达到`terminal state`之前提前结束`episode`。
- **info**(*dictionary*)- `info` 中包含辅助诊断信息(有助于调试、学习和日志记录)。例如，这可能包含： 
描述`agent`的性能状态的度量，从观测中隐藏的变量，或者组合产生总奖励的单个奖励项。它也可以包含区分截断和终止的信息，但这是不赞成返回两个布尔值，并将在未来的版本中删除。
- (废弃的)
- **done**(*bool*) - 如果`episode`已经结束，则为一个布尔值，在这种情况下，再次调用`step()`将返回未定义的结果。 
一个`done`信号可能是由于不同的原因发出的：可能是环境下的任务解决成功，超过了一定的时间限制，或者是物理模拟进入了无效状态。
 
### `gym.Env.reset(self, *, seed: Optional[int] = None, options: Optional[dict] = None) → Tuple[ObsType, dict]`

将环境重置为初始状态并返回初始观测值。

该方法可以在`seed`为整数或者环境尚未初始化随机数发生器的情况下重置环境的随机数发生器。
如果环境中已经有随机数发生器，并且使用`seed = None`调用了`reset ()`，则RNG（随机数发生器）不应该被重置。
此外，`reset()`应该在初始化后立即用一个整数`seed`调用(在典型用例中)，然后不再调用。

**参数**：
- **seed**(*optional int*) - 用于初始化环境的伪随机数生成器（PRNG）的`seed`。
如果环境中还没有一个伪随机数生成器（PRNG）并且传递`Seed = None` (默认选项)，
则从某个熵源(例如时间戳或/dev/urandom)中选择一个种子。但是，如果环境已经有一个PRNG并且传递`seed= None`， 
则不会重置PRNG。如果传递一个整数，即使已经存在，PRNG也会被重置。通常情况下，在环境初始化后传递一个整数，然后再也不传递参数。
请参阅上面的例子，看看这个模板再行动。
- **options**(*optional dict*) - 额外的信息来指定环境如何重置(可选,视具体环境而定)

**返回值**：
- **observation**(*object*) - 初始状态的`observation`。这将是`observation_space`(通常是一个numpy数组)中的一个元素，类似于step( )返回的`observation`
- **info**(*dictionary*) - 此词典包含补充`observation`的辅助信息。它应该类似于`step()`返回的信息。

### `gym.Env.render(self) → Optional[Union[RenderFrame, List[RenderFrame]]]`

在环境初始化过程中，计算由`render_mode`属性指定的渲染帧。
支持模式的集合因环境而异,而且一些第三方环境可能根本不支持渲染。按照惯例，如果`render_mode`为：

- `None(default)`： 不需要计算渲染帧
- `human`：`render`返回None。环境在当前的显示器或终端中不断呈现。通常为用户使用。
- `rbg_array`：返回表示环境当前状态的单帧。一帧是一个形状为`(x ,y ,3)`的numpy.ndarray，表示x行y列像素图像的RGB值。
- `rgb_array_list`：返回上次重置以来表示环境状态的帧列表。与rgb _ array一样，每一帧是一个形状为`(x ,y ,3)`的numpy.ndarray. nd阵列。
- `ansi`：返回一个字符串(str)或StringIO。StringIO为每个时间步包含一个终端风格的文本表示。文本可以包括换行符和ANSI逃逸序列(例如对于颜色)。
    
    > **note**:
     确保类的元数据'render_modes'键包含支持的模式列表。建议在实现中调用super ( )来使用该方法的功能。 
    

## Attributes

### `Env.action_space: Space[ActType]`
该属性给出了有效`action`的格式。它是Gym提供的数据类型空间。
例如，如果动作空间是离散型的，并且给定值`Discrete(2)`，这意味着存在两个有效的离散动作：0和1。

    >>> env.action_space
    Discreate(2)
    >>> env.observation_space
    Box(-3.4028234663852886e+38, 3.4028234663852886e+38, (4,), float32)

### `Env.observation_space: Space[ObsType]`
该属性给出了有效`observation`的格式。它是Gym提供的数据类型空间。
例如，如果观测空间为`Box`型且对象的形状为( 4 ,)，则表示一个有效的观测将是一个包含4个数字的数组。我们也可以用属性检查`box`的边界。


    >>> env.observation_space.high
    array([4.8000002e+00, 3.4028235e+38, 4.1887903e-01, 3.4028235e+38], dtype=float32)
    >>> env.observation_space.low
    array([-4.8000002e+00, -3.4028235e+38, -4.1887903e-01, -3.4028235e+38], dtype=float32)

### `Env.reward_range = (-inf, inf)`
该属性是一个元组，对应最小和最大的可能奖励。默认范围设置为`( -inf , + inf)`。如果想要更窄的范围，可以设定。

## Additional Methods

### `gym.Env.close(self)`

覆盖子类中的close以执行任何必要的清理。

当`garbabge collected`或程序退出时，环境会自动`close()`自己。

## gym.Wrapper

### `class gym.Wrapper(env: Env)`
封装一个环境，允许对`step ()`和`reset ()`方法进行模块化转换。

该类是所有包装器的基类。该子类可以覆盖一些方法来改变原始环境的行为而不触及原始代码。
> note 如果子类重写了`__init__ ()`，不要忘记调用super().__init__(env)`。


## gym.ObservationWrapper

### `class gym.ObservationWrapper(env: Env)`

可以使用`observation()`修改观测值以`reset( )`和`step( )`的`warppers`超类。
如果想要将一个函数应用到基环境返回的观测中，然后再将其传递给学习代码，
可以简单地从`ObservWrapper`继承并改写方法`observation()`来实现该转换。
该方法定义的变换必须在基准环境的观测空间上定义。然而，它可能会在不同的空间中获得值。
在这种情况下，您需要通过在`wrapper`的__init__( )方法中设置
`self.observer_space`来指定`wrapper`的新观测空间。
例如，您可能有一个2D导航任务，其中环境返回字典作为观测，键`agent_position`和`target _ position`。
一个常见的做法可能是舍弃部分自由度，只考虑目标相对于智能体的位置，
即`observation[ "targer_position"]` -`observation[ "agent_posion"]`。为此，可以实现类似这样的`observation wrapper`：

    class RelativePosition(gym.ObservationWrapper):
    def __init__(self, env):
        super().__init__(env)
        self.observation_space = Box(shape=(2,), low=-np.inf, high=np.inf)

    def observation(self, obs):
        return obs["target"] - obs["agent"]
其中，Gym提供了观测包装器`TimeAwareObception`，为观测添加了关于`time-step`索引的信息。