let state = {
  calendarEl: null,
  todos: [
    {
      id: 1,
      text: 'Learn FullCalendar',
      completed: true,
      start: '2018-06-21'
    },
    {
      id: 2,
      text: 'Learn Mithril',
      completed: false,
      start: '2018-06-22'
    },
    {
      id: 3,
      text: 'Profit',
      completed: false,
      start: '2018-06-23'
    },
  ],
  todo: null,
  todoDate: null,
  setTodo(value) {
    state.todo = value
  },
  setTodoDate(value) {
    state.todoDate = value
  },
  createTodo() {
    let newTodo = {
      id: state.todos.length + 1,
      text: state.todo,
      completed: false,
      start: state.todoDate
    }
    
    console.log(newTodo)
    
    state.todos.push(newTodo)
    
    $(state.calendarEl).fullCalendar('addEventSource', {
      events: [
        {
          title: state.todo,
          start: state.todoDate
        }
      ],
      
      allDayDefault: true
    })
    
    state.todo = ''
    state.todoDate = ''
  },
  
  completeTodo(todo) {
    let foundTodoIndex = _.findIndex(state.todos, {id: todo.id})
    
    state.todos.splice(foundTodoIndex, 1, {
      id: todo.id,
      text: todo.text,
      start: todo.start,
      completed: true
    })
  },
  
  uncompleteTodo(todo) {
    let foundTodoIndex = _.findIndex(state.todos, {id: todo.id})
    
    state.todos.splice(foundTodoIndex, 1, {
      id: todo.id,
      text: todo.text,
      start: todo.start,
      completed: false
    })
  }
}

let Calendar = {
  oncreate(vnode) {
    $(vnode.dom).fullCalendar()
    state.calendarEl = vnode.dom
  },
  
  view() {
    return m('div')
  }
}

let Todo = {
  view() {
    return [
      m('.columns', [
        m('.column.col-12', [
          m('.panel', [
            m('.panel-header', m('h2', 'Todos')),
            m('.panel-body', [
              m('div', state.todos
                .filter((todo) => {
                   return todo.completed == false
                })
                .map((todo) => {
                return m('.form-group', [
                  m('label.form-checkbox', [
                    m('input', {
                      key: todo.id,
                      type: 'checkbox',
                      checked: false,
                      onclick: () => {
                        state.completeTodo(todo)
                      }
                    }),
                    m('i.form-icon'),
                    todo.text
                  ])
                ])
              }))
            ]),
            m('.panel-footer', [
              m('.input-group', [
                m('input.form-input', {
                  placeholder: 'Some amazing task',
                  oninput: m.withAttr('value', state.setTodo),
                  value: state.todo
                }),
                m('button.btn.btn-primary.input-group-btn', {
                  onclick: state.createTodo
                }, 'Save')
              ]),
              m('.input-group', [
                m('input.form-input', {
                  style: 'margin-top: 15px;',
                  type: 'date',
                  oninput: m.withAttr('value', state.setTodoDate),
                  value: state.todoDate
                }, )
              ])
            ])
          ])
        ]),
        m('.column.col-12', {
          style: 'margin-top: 15px;'
        }, [
          m('.panel', [
            m('.panel-header', m('h2', 'Completed Todos')),
            m('.panel-body',  m('div', state.todos
                .filter((todo) => {
                   return todo.completed == true
                })
                .map((todo) => {
                return m('.form-group', [
                  m('label.form-checkbox', [
                    m('input', {
                      key: todo.id,
                      type: 'checkbox',
                      onclick: () => {
                        state.uncompleteTodo(todo)
                      },
                      checked: true
                    }),
                    m('i.form-icon'),
                    m('span', {
                      style: 'text-decoration: line-through'
                    }, todo.text)
                  ])
                ])
              })))
          ])  
        ])
      ])
    ]
  }
}

let App = {
  view() {
    return m('.container', [
      m('.columns', [
        m('.column.col-7', m(Calendar)),
        m('.column.col-5', m(Todo))
      ])
    ])
  }
}

m.mount(document.getElementById('app'), App)