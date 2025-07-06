path('interaction/', include('interaction.urls')),

path('todo/detail/<int:pk>/', todo_detail_with_interaction, name='todo_detail'),


