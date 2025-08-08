# PYTHON script
import os
import ansa
from ansa import base, constants, mesh

def main():
	# Need some documentation? Run this with F5

	help_html = os.path.join(ansa.constants.app_root_dir.replace('/', os.path.sep), '..', 'ansa_v23.1.2', 'docs', 'extending', 'python_api', 'html', 'index.html')
	print('Documentation HTML: '+ help_html)

	# Get the current deck
	current_deck = base.CurrentDeck()
	print("Current deck:", current_deck)
	
	faces = base.CollectEntities(current_deck, None, "FACE")
	shells = base.CollectEntities(current_deck, None, "SHELL")

	print(shells)

	options = {
		"align_middle": "5%",
		"align_boundary": "5%",
		"align_thickness": "5%",
		"align_empty_areas": "",
		"align_empty_perimeters": "",
		"incompatible": "10%",
		"nodal_thickness": "50%",
		"solid_middle": "5%",
		"solid_boundary": "5%",
		"missing_mass": "",
	}

	ret = mesh.CheckMiddleMesh(
		shells,
		faces,
		options,
		check_for_unconnected=True,
		return_ents=True,
		min_nodal_thick=0.0,
	)
	
	print(f"The following failed the check: {ret.keys()}")
	
	
	parts_array = base.CollectEntities(current_deck, None, "ANSAPART")
	
	#for part in parts_array:
	#	off_element_dict = base.CalculateOffElements(part)
	#	print(off_element_dict)
	

	# Function will print the off solids per criterion calculated on whole model
	PrintNumOffShellsPerCriterion()

    
# example 4 (like example 3, but more detailed output)
def PrintNumOffShellsPerCriterion():
	off_elements = base.CalculateOffElements("Shells", True)
	print(off_elements)


	
if __name__ == '__main__':
	main()


