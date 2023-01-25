       result = ''
       ak_number = models.Entry.objects.filter(
           event=request.POST.get('event'), ak_number=self.request.POST['AK']).exists()
       np_number = models.Entry.objects.filter(
           event=request.POST.get('event'), np_number=self.request.POST['NP']).exists()

       if self.request.POST['AK'] is not '':
           if re.match(r"^[0-9]{8}$", self.request.POST['AK']) is not None:
               if ak_number:
                   result = '{}は既に登録されています'.format(self.request.POST['AK'])
#                    ng = 'NG'
               else:
                   if self.request.POST['NP'] == '':
                       for event in models.Event.objects.filter(id=request.POST.get('event')):
                           models.Entry.objects.get_or_create(
                               ak_number=self.request.POST['AK'], event=event)
                           result = '{}を登録しました'.format(self.request.POST['AK'])
                           ok = 'OK'
           else:
               result = '8桁の半角数字を入力してください'
               ng = 'NG'

       if self.request.POST['NP'] is not '':
           if re.match(r"^[0-9]{8}$", self.request.POST['NP']) is not None:
               if np_number:
                   result = '{}は既に登録されています'.format(self.request.POST['NP'])
                   ng = 'NG'
               else:
                   if self.request.POST['AK'] == '':
                       for event in models.Event.objects.filter(id=request.POST.get('event')):
                           models.Entry.objects.get_or_create(
                               np_number=self.request.POST['NP'], event=event)
                           result = '{}を登録しました'.format(self.request.POST['NP'])
                           ok = 'OK'
           else:
                   result = '8桁の半角数字を入力してください'
                   ng = 'NG'

       if self.request.POST['AK'] == '' and self.request.POST['NP'] == '':
           result = '値を入力してください'
           ng = 'NG'
       elif self.request.POST['AK'] != '' and self.request.POST['NP'] != '':
           result = 'どちらかに入力してください'
           ng = 'NG'

       return self.render_to_response(self.get_context_data(result=result, ok=ok, ng=ng))
