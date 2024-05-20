from pages.base_page import BasePage
from data.links import DESIRE_FITNESS_TEE_URL


class Header(BasePage):

    def visit_desire_fitness_tee_page(self):
        self.visit(DESIRE_FITNESS_TEE_URL)
