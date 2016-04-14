# flask restful

## 方法预览

HTTP 方法  |URL                                              |动作
--------- | -------------------------------------------------|-------------
GET       |  http://[hostname]/todo/api/v1.0/tasks           | 检索任务列表
GET       |  http://[hostname]/todo/api/v1.0/tasks/[task_id] | 检索某个任务
POST      |  http://[hostname]/todo/api/v1.0/tasks           | 创建新任务
PUT       |  http://[hostname]/todo/api/v1.0/tasks/[task_id] | 更新任务
DELETE    |  http://[hostname]/todo/api/v1.0/tasks/[task_id] | 删除任务

* 运行
```bash
python app.py
```

## API访问

* 查询所有tasks
```bash
curl -i http://localhost:5000/todo/api/v1.0/tasks
```

* 根据ID查询task
```bash
curl -i http://localhost:5000/todo/api/v1.0/tasks/1
```


* 新增tasks
```bash
curl -i -H "Content-Type: application/json" -X POST -d '{"title":"Read a book"}' http://localhost:5000/todo/api/v1.0/tasks
```

* 修改task
```bash
curl -i -H "Content-Type: application/json" -X PUT -d '{"done":true}' http://localhost:5000/todo/api/v1.0/tasks/2
```

* 删除task
```bash
curl -i -X delete http://127.0.0.1:5000/todo/api/v1.0/tasks/1
```


