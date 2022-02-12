import random
import urllib.request
from PIL import Image
from io import BytesIO

from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from server.questions.models import Question, QuestionMedia, SolutionMedia

answers = ["O(n^2)", "O(n)", "O(nlogn)", "O(logn)"]
question_texts = ["""
Donec pharetra ipsum at nibh lacinia, et efficitur tellus consequat. Quisque non dolor venenatis ipsum dapibus efficitur. Quisque non dui nisl. Donec in odio quam. Morbi egestas eget orci ultricies tincidunt. Fusce viverra aliquam malesuada. Vestibulum a enim at magna interdum ullamcorper quis fringilla est. Suspendisse accumsan pellentesque leo at pretium. Sed tempor mauris at elementum maximus. Nulla facilisi.

Donec luctus convallis lorem, quis tristique massa aliquet in. Vestibulum mollis consectetur tincidunt. Nullam est dolor, feugiat eu hendrerit vel, eleifend ac metus. Fusce at mollis ipsum, vitae euismod felis. Duis volutpat pretium urna, vitae aliquet est feugiat ut. Etiam condimentum, orci eu tempor cursus, eros lacus semper augue, id tincidunt metus nisl a ex. Nulla pharetra metus eget hendrerit faucibus. Cras molestie enim lobortis elit egestas, at fringilla arcu imperdiet. Suspendisse elementum, ex nec tempor molestie, lacus nunc feugiat ligula, sed aliquet turpis lectus vitae tortor. Sed facilisis lacinia maximus.

""",
"""
Etiam erat libero, commodo et feugiat a, imperdiet ac ipsum. Fusce rutrum consectetur nisl, quis ullamcorper quam sodales sit amet. Integer sed volutpat orci. Morbi eu urna tristique, vestibulum risus et, auctor quam. In mi tortor, faucibus ornare tristique at, maximus et nunc. Nulla ante mi, volutpat ac vulputate nec, convallis id ante. Curabitur vestibulum consectetur ligula ut tristique. Suspendisse nec libero eget augue consectetur aliquam. Fusce et mauris et ex rutrum iaculis et id massa. Ut ac posuere mi, nec pretium purus. Vivamus enim sem, faucibus quis tempus in, venenatis non lacus. Nam dapibus ante ut feugiat imperdiet. Mauris dignissim, nulla quis congue pretium, lorem elit consequat massa, at aliquet orci lorem eget urna. Fusce ac imperdiet neque, et viverra enim.
""",
"""
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur ullamcorper porttitor urna, ut vestibulum velit accumsan condimentum. Interdum et malesuada fames ac ante ipsum primis in faucibus. Suspendisse laoreet, dolor eu condimentum aliquet, dui nibh lacinia tellus, vitae dignissim est erat a nulla. Donec tempus, augue et iaculis condimentum, est ex tristique velit, sit amet rutrum purus metus at leo. Morbi lacinia nunc id dolor consectetur, imperdiet feugiat lectus vestibulum. Curabitur mattis risus turpis, at facilisis mi rutrum vel. Vivamus interdum, ipsum ac hendrerit malesuada, risus metus elementum elit, vel hendrerit elit lectus sit amet metus. Donec eu fermentum diam.

Aliquam sem purus, posuere at pellentesque ut, rhoncus a tellus. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Quisque non nisi quam. In eget tempus ante. Cras tincidunt, ipsum porta convallis rutrum, risus nisi rhoncus neque, a interdum arcu nisi eu tortor. Fusce cursus erat ut felis vehicula imperdiet. Integer vel venenatis urna. Nullam a turpis lobortis, aliquam neque et, laoreet nibh. Praesent dapibus arcu vel est dapibus, vulputate posuere nulla aliquam. Aliquam vel ultrices arcu.
"""]


def download_image(name, image, url):
    input_file = BytesIO(urllib.request.urlopen(url).read())
    output_file = BytesIO()
    img = Image.open(input_file)
    if img.mode != "RGB":
        img = img.convert("RGB")
    img.save(output_file, "JPEG")
    image.save(name+".jpg", ContentFile(output_file.getvalue()), save=False)



class Command(BaseCommand):
    help = "Create test data"


    def handle(self, *args, **options):
        for i in range(1, 20):

            q = Question.objects.create(question_title=f"Question {i}",
                                        question_text=random.choice(question_texts),
                                        solution_answer=random.choice(answers),
                                        solution_text=random.choice(question_texts),
                                        difficulty=Question.Difficulty.MEDIUM)
            # q.question_medias.add([q_media_1])
            # q.solution_medias.set(sol_medias)

            for j in range(1, 3):
                image_id = f"{i}{j}"
                q_media = QuestionMedia(label=f"image-{image_id}")
                url = f"https://picsum.photos/id/{image_id}/200/300"
                download_image(image_id, q_media.media, url)
                q_media.save()
                q.question_medias.add(q_media)

            for j in range(3, 5):
                image_id = f"{i}{j}"
                sol_media = SolutionMedia(label=f"image-{image_id}")
                url = f"https://picsum.photos/id/{image_id}/200/300"
                download_image(image_id, sol_media.media, url)
                sol_media.save()
                q.solution_medias.add(sol_media)

            q.save()

            self.stdout.write(self.style.SUCCESS(f"Successfully created question {q.question_title}"))

