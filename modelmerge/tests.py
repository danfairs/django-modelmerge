from django.test import TestCase


class SetUp(TestCase):

    def setUp(self):
        from testapp.models import Customer, Notes, Pizza, Topping
        self.cheese = Topping.objects.create(name='Cheese')
        self.tomatoes = Topping.objects.create(name='Tomatoes')
        self.mushrooms = Topping.objects.create(name='Mushrooms')
        self.jalapenos = Topping.objects.create(name='jalapenos')

        self.alex = Customer.objects.create(name='Alex')
        self.barbara = Customer.objects.create(name='Barbara')
        self.charlie = Customer.objects.create(name='Charlie')

        self.margherita = Pizza.objects.create(
            name='Margherita',
            size=10,
            customer=self.alex,
            notes=Notes.objects.create(text='Deliver asap')
        )
        self.margherita.toppings = [self.cheese, self.tomatoes]

        self.funghi = Pizza.objects.create(
            name='Funghi',
            size=12,
            customer=self.barbara,
            notes=Notes.objects.create(text='Deliver to top bell')
        )
        self.funghi.toppings = [self.mushrooms]

        self.volcano = Pizza.objects.create(
            name='Margherita',
            size=10,
            customer=self.charlie,
            notes=Notes.objects.create(text='Deliver at 11pm')
        )
        self.volcano.toppings = [self.cheese, self.tomatoes, self.jalapenos]


class MergeFormTestCase(SetUp):

    def test_defaults(self):
        """ A default merge should define a merge that merges all fields,
        doesn't allow specifying an alternate value, and will create a new
        instance with the merged data.
        """
        from modelmerge import merge
        from testapp.models import Pizza

        class DefaultMerge(merge.Merge):
            class Meta:
                model = Pizza

        merge = DefaultMerge(merge=(self.pizza_1, self.pizza_2))
        form = merge.form_class()

        # We should find 12 fields, 2 for each of the fields on the source
        # model
        self.assertEqual(12, len(form.fields))
