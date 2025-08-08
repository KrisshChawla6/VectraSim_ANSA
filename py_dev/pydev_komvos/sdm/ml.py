from __future__ import annotations
from typing import *

class RunCollection():

	"""

	A collection of Experiment Simulation Runs

	See Also
	--------
	sdm.ml.Dataset, sdm.ml.Predictor, sdm.ml.ModeClassifier

	Examples
	--------
	::

		# PYTHON script
		import sdm
		from sdm import ml
		
		
		# Using a DOE Study sid
		def main_doe_study():
		    sids = [25]
		    run_collection = ml.RunCollection(sids)
		
		
		# Using Simulation Run sids
		def main_sim_runs():
		    sids = list(range(3, 13))
		    run_collection = ml.RunCollection(sids)
		
		
		# Interested in 2d/3d results too
		def main_2d3d():
		    sids = list(range(3, 13))
		    result_file = "d3plot"
		    curve_result_file = "binout"
		    run_collection = ml.RunCollection(sids, result_file, curve_result_file)
		
		
		# Using custom features as inputs - through csv file
		def main_extras_csv():
		    sids = list(range(3, 13))
		    result_file = "d3plot"
		    curve_result_file = "binout"
		    extras_csv = "/path/to/extras_example.csv"
		    extras_callback = None
		    run_collection = ml.RunCollection(
		        sids, result_file, curve_result_file, extras_csv, extras_callback
		    )
		
		
		# Using custom features as inputs - through callback
		def main_extras_callback():
		    sids = list(range(3, 13))
		    result_file = "d3plot"
		    curve_result_file = "binout"
		    extras_csv = None
		    extras_callback = ["/path/to/extras_callback_file.py", "function_name"]
		    run_collection = ml.RunCollection(
		        sids, result_file, curve_result_file, extras_csv, extras_callback
		    )

	"""


	runs: object = None
	"""
	A dictionary with the Simulation Run objects contained in the RunCollection, using the server ids of the Simulation Runs as keys.

	"""

	doe_studies: object = None
	"""
	A dictionary with the DOE Study objects contained in the RunCollection, using the server ids of the DOE Studies as keys.

	"""

	result_file: str = None
	"""
	The result file name for loading the field (3d) results, if needed. None otherwise.

	"""

	curve_result_file: str = None
	"""
	The result file name for loading the curve (2d) results, if needed. None otherwise.

	"""

	extras_names: object = None
	"""
	A list of the names of the custom extra features, if any are given through csv or callback.
	In the case of csv, the 1st row of the csv file contains the names of those custom features and the 1st column specifies the server id of the Sim Run they corresponds to.
	In the case of the callback, the features are named after the callback function. The user must specify the file and the function name of the callback. The function must return a list.
	Note: these custom features will be used as extra inputs only in DV-based tasks.

	"""

	def get_sids(self) -> object:

		"""

		Returns a list of the server ids of the Simulation Runs contained in the RunCollection


		Returns
		-------
		object

		"""


	def get_doe_study_sids(self) -> object:

		"""

		Returns a list of the server ids of the DOE Studies contained in the RunCollection


		Returns
		-------
		object

		"""


	def get_dv_names(self) -> object:

		"""

		Returns a list with the names of the Design Variables of the RunCollection


		Returns
		-------
		object

		"""


	def get_input_names(self) -> object:

		"""

		Returns a list of the inputs used by the RunCollection


		Returns
		-------
		object
			If no extras have been given then the inputs are the names of the Design Variables

		"""


	def print_self(self) -> object:

		"""

		Prints the contents of the RunCollection


		Returns
		-------
		object

		"""

class Dataset():

	"""

	A collection of Experiment Simulation Runs with information about the responses of interest. It can be used as input for training tasks.

	See Also
	--------
	sdm.ml.RunCollection, sdm.ml.Predictor

	Examples
	--------
	::

		# PYTHON script
		import sdm
		from sdm import ml
		
		
		# Only 1d responses
		def main_1d():
		    sids = [25]
		    run_collection = ml.RunCollection(sids)
		
		    responses = [
		        "First_Torsional_value",
		        "First_Vertical_Bending_value",
		        "First_Lateral_Bending_value",
		    ]
		    data = ml.Dataset(run_collection, responses)
		
		    predictor = ml.Predictor("group_name")
		    sub_type = "fb"  # or 'dv'
		    new_predictor_sids = predictor.train(data, sub_type)
		
		
		# Interested in 2d/3d results too
		def main_1d2d3d():
		    sids = list(range(3, 13))
		    result_file = "d3plot"
		    curve_result_file = "binout"
		    run_collection = ml.RunCollection(sids, result_file, curve_result_file)
		
		    responses = ["max_intrusion", "Kinetic energy (ke)", "Displacements"]
		    response_types = ["keyvalue", "curve", "field"]
		    response_subtypes = [None, "glstat-Global", "Deformation"]
		    data = ml.Dataset(run_collection, responses, response_types, response_subtypes)
		
		    predictor = ml.Predictor("group_name")
		    sub_type = "dv"
		    new_predictor_sids = predictor.train(data, sub_type)

	"""


	run_collection: object = None
	"""
	The RunCollection used to create the Dataset.

	"""

	response_names: object = None
	"""
	A list of the responses names to be used a targets.

	"""

	response_types: object = None
	"""
	A list of the response Output Types.

	"""

	response_subtypes: object = None
	"""
	A list of the response Output SubTypes.

	"""

	entities_selection_mode: object = None
	"""
	A dictionary with the curve entity selection mode for each curve sub-type, using the curve sub-types as keys. Used only for curve (2d) responses in NASTRAN DMs.

	"""

	curve_x_axis: object = None
	"""
	A dictionary with the curve x-axis data for each curve sub-type, using the curve sub-types as keys. Used only for curve (2d) responses in NASTRAN DMs.

	"""
class Predictor():

	"""

	A Machine Learning Predictor used for training or prediction tasks.

	See Also
	--------
	sdm.ml.RunCollection, sdm.ml.Dataset, sdm.ml.ModeClassifier

	Examples
	--------
	::

		# TRAIN
		import sdm
		from sdm import ml
		
		
		def main():
		    sids = [25]
		    result_file = "d3plot"
		    curve_result_file = "binout"
		    run_collection = ml.RunCollection(sids, result_file, curve_result_file)
		
		    responses = ["max_intrusion", "Kinetic energy (ke)", "Displacements"]
		    response_types = ["keyvalue", "curve", "field"]
		    response_subtypes = [None, "glstat-Global", "Deformation"]
		    data = ml.Dataset(run_collection, responses, response_types, response_subtypes)
		
		    predictor = ml.Predictor("group_name")
		    new_predictor_sids = predictor.train(data, "dv")
		
		
		if __name__ == "__main__":
		    main()
		
		# --------------
		# PREDICT
		import sdm
		from sdm import ml
		
		
		# Predict with Sim Runs server ids
		def main1():
		    sids = [3, 4]
		    predictor = ml.Predictor("group_name")
		    predictions = predictor.predict(sids=sids)
		    return predictions
		
		
		# Predict with RunCollection object
		def main2():
		    sids = [3, 4]
		    result_file = "d3plot"
		    curve_result_file = "binout"
		    run_collection = ml.RunCollection(sids, result_file, curve_result_file)
		    predictor = ml.Predictor("group_name")
		    predictions = predictor.predict(run_collection=run_collection)
		    return predictions
		
		
		# Predict with specific DV values (only for DV-based)
		def main3():
		    external = [[10.4896, 2.37], [7.773, 1.81], [9.1122, 1.72]]
		    predictor = ml.Predictor("group_name_dv")
		    predictions = predictor.predict(external=external)
		    return predictions
		
		
		# Predict with specific input files (only for Feature-based)
		def main4():
		    external = ["/path/to/model_1.ansa", "/path/to/model_2.ansa"]
		    predictor = ml.Predictor("group_name_fb")
		    predictions = predictor.predict(external=external)
		    return predictions
		
		
		if __name__ == "__main__":
		    predictions = main1()
		    # predictions = main2()
		    # predictions = main3()
		    # predictions = main4()
		
		    print(predictions.predictions)
		    print(predictions.variances)
		
		# --------------
		# RE-TRAIN
		import sdm
		from sdm import ml
		
		
		def main():
		    sids = [26]
		    result_file = "d3plot"
		    curve_result_file = "binout"
		    run_collection = ml.RunCollection(sids, result_file, curve_result_file)
		
		    predictor = ml.Predictor("group_name")
		    incremental_support = True
		    new_predictor_sids = predictor.re_train(
		        run_collection, incremental_support=incremental_support
		    )
		
		
		if __name__ == "__main__":
		    main()
		
		# --------------
		# INCREMENTAL TRAIN
		import sdm
		from sdm import ml
		
		
		def main():
		    sids = [26]
		    result_file = "d3plot"
		    curve_result_file = "binout"
		    run_collection = ml.RunCollection(sids, result_file, curve_result_file)
		
		    predictor = ml.Predictor("group_name")
		    new_predictor_sids = predictor.incremental_train(run_collection)
		
		
		if __name__ == "__main__":
		    main()
		
		
		# --------------
		# IMPROVE
		import sdm
		from sdm import ml
		
		
		def main():
		    predictor = ml.Predictor("group_name")
		    n_additional = 10
		    new_predictor_sids = predictor.improve(n_additional)
		
		
		if __name__ == "__main__":
		    main()

	"""


	name: str = None
	"""
	The name of the Predictor Group.

	"""

	def train(self, dataset: object, sub_type: str, incremental_support: bool) -> list:

		"""

		Trains the Predictor. The input Simulation Runs and the selected responses are specified by a Dataset object. Training can be either DV-based or Feature-based. Training is asynchronous.


		Parameters
		----------
		dataset : object
			A Dataset object that specifies the input Simulation Runs and the selected responses.

		sub_type : str, optional
			The predictor Sub-Type, e.g. DV based or Feature based. 
			Accepted values for DV based are: 'dv', 'dv-based', 'dv_based'.
			Accepted values for Feature based are: 'fb', 'feature', 'feature-based', 'feature_based'.
			Default value is DV based training.

		incremental_support : bool, optional
			Whether or not the predictor should support Incremental Training. 
			Default value is False.

		Returns
		-------
		list
			Returns a list of the server ids of the created predictor(s).

		"""


	def predict(self, sids: list, run_collection: object, external: list) -> tuple:

		"""

		Runs a prediction on the specified input, which can be one of the following: A list of server ids of Simulation Runs, a RunCollection object or external data.


		Parameters
		----------
		sids : list, optional
			A list of server ids (integers) of Simulation Runs.

		run_collection : object, optional
			A RunCollection object.

		external : list, optional
			A list of external data. 
			For DV-based predictors this means a list of DV values lists. 
			For Feature-based predictors this means a list of paths to input files.

		Returns
		-------
		tuple
			Returns a namedtuple object with the following fields: predictions, variances and prediction_sids. Keyvalue (1d) predictors provide predictions and variances, while Curve (2d) and Field (3d) predictors provide Prediction Simulation Run server ids.

		"""


	def re_train(self, run_collection: object, incremental_support: bool) -> list:

		"""

		Re-trains a Predictor with new data. The new data are specified by a RunCollection object. The resulting Predictor can either support Incremental Training or not. Training is asynchronous.


		Parameters
		----------
		run_collection : object
			A RunCollection object that specifies the input Simulation Runs.

		incremental_support : bool, optional
			Whether or not the predictor should support Incremental Training. 
			Default value is False.

		Returns
		-------
		list
			Returns a list of the server ids of the created predictor(s).

		"""


	def incremental_train(self, run_collection: object) -> list:

		"""

		Incrementally trains a Predictor with new data. The new data are specified by a RunCollection object. Training is asynchronous.


		Parameters
		----------
		run_collection : object
			A RunCollection object that specifies the input Simulation Runs.

		Returns
		-------
		list
			Returns a list of the server ids of the created predictor(s).

		"""


	def improve(self, n_additional: int) -> list:

		"""

		Improves a group of Predictors with new data. The new data are new experiments optimally selected through smart sampling. The new experiments are added one at a time, i.e. the optimization task executes for each new experiment and the predictor is improved adding each new experiment iteratively. Improve is only supported for DV-based predictors (incremental and feature based are not supported).


		Parameters
		----------
		n_additional : int
			The number of new experiments to be selected for improving the predictor group (integer >=1)

		Returns
		-------
		list
			Returns a list of the server ids of the created predictor(s).

		"""

class ModeClassifier():

	"""

	A Machine Learning Classifier that can be trained to label modes of Simulation Runs solved for modal analysis.

	See Also
	--------
	sdm.ml.RunCollection, sdm.ml.Predictor

	Examples
	--------
	::

		# TRAIN
		import sdm
		from sdm import ml
		
		
		def main():
		    sids = list(range(3, 13))
		    result_file = "model.op2"
		    curve_result_file = "model.op2"
		    run_collection = ml.RunCollection(sids, result_file, curve_result_file)
		
		    mode_labels = "/path/to/mode/labels.csv"
		    predictor = ml.ModeClassifier("group_name")
		    new_predictor_sids = predictor.train(run_collection, mode_labels=mode_labels)
		
		
		if __name__ == "__main__":
		    main()
		
		# --------------
		# PREDICT
		import sdm
		from sdm import ml
		
		
		# Predict with Sim Runs server ids
		def main1():
		    sids = [3, 4]
		    predictor = ml.ModeClassifier("group_name")
		    predictions = predictor.predict(sids=sids)
		    # or
		    predictions = predictor.predict(sids=sids, mode_numbers=[7, 8, 9])
		    return predictions
		
		
		# Predict with RunCollection object
		def main2():
		    sids = [3, 4]
		    result_file = "model.op2"
		    curve_result_file = "model.op2"
		    run_collection = ml.RunCollection(sids, result_file, curve_result_file)
		    predictor = ml.ModeClassifier("group_name")
		    predictions = predictor.predict(run_collection=run_collection)
		    # or
		    predictions = predictor.predict(
		        run_collection=run_collection, mode_numbers=[7, 8, 9]
		    )
		    return predictions
		
		
		# Predict with external result files
		def main3():
		    external = ["/path/to/model1.op2", "/path/to/model2.op2", "/path/to/model3.op2"]
		    predictor = ml.ModeClassifier("group_name")
		    predictions = predictor.predict(external=external)
		    # or
		    predictions = predictor.predict(external=external, mode_numbers=[7, 8, 9])
		    return predictions
		
		
		if __name__ == "__main__":
		    predictions = main1()
		    # predictions = main2()
		    # predictions = main3()
		
		    print(predictions.predictions)
		
		# --------------
		# RE-TRAIN
		import sdm
		from sdm import ml
		
		
		def main():
		    sids = list(range(14, 24))
		    result_file = "model.op2"
		    curve_result_file = "model.op2"
		    run_collection = ml.RunCollection(sids, result_file, curve_result_file)
		
		    mode_labels = "/path/to/mode/labels.csv"
		    predictor = ml.ModeClassifier("group_name")
		    new_predictor_sids = predictor.re_train(run_collection, mode_labels=mode_labels)
		
		
		if __name__ == "__main__":
		    main()

	"""


	name: str = None
	"""
	The name of the Predictor Group.

	"""

	def train(self, run_collection: object, mode_labels: str=None) -> list:

		"""

		Trains the ModeClassifier. The input Simulation Runs are specified by a RunCollection object. The labels of the modes of those Simulation Runs can be specified either by Mode_Labels reports (Table) in each Run or by a csv file with labels for all Runs. Training is asynchronous.


		Parameters
		----------
		run_collection : object
			A RunCollection object that specifies the input Simulation Runs and their result files.

		mode_labels : str, optional
			The path of the csv file that specifies the mode labels for all the Simulation Runs that will be used for training.
			The file must be structured as follows:
			Sim Run Id, Mode number, Mode label
			3, 7, torsional
			3, 8, lateral_bending
			4, 7, torsional
			4, 8, vertical_bending
			If the Simulation Runs of the training set contain Mode_Labels reports, then the mode_labels argument can be skipped.

		Returns
		-------
		list
			Returns a list of the server ids of the created predictor(s).

		"""


	def re_train(self, run_collection: object, mode_labels: str) -> list:

		"""

		Re-trains a ModeClassifier with new data. The new data are specified by a RunCollection object. Training is asynchronous.


		Parameters
		----------
		run_collection : object
			A RunCollection object that specifies the input Simulation Runs and their result files.

		mode_labels : str, optional
			The path of the csv file that specifies the mode labels for all the Simulation Runs that will be used for training.
			The file must be structured as follows:
			Sim Run Id, Mode number, Mode label
			3, 7, torsional
			3, 8, lateral_bending
			4, 7, torsional
			4, 8, vertical_bending
			If the Simulation Runs of the training set contain Mode_Labels reports, then the mode_labels argument can be skipped.

		Returns
		-------
		list
			Returns a list of the server ids of the created predictor(s).

		"""


	def predict(self, sids: list, run_collection: object, external: list, mode_numbers: list) -> tuple:

		"""

		Runs a prediction on the specified input, which can be one of the following: A list of server ids of Simulation Runs, a RunCollection object or external data.


		Parameters
		----------
		sids : list, optional
			A list of server ids (integers) of Simulation Runs.

		run_collection : object, optional
			A RunCollection object.

		external : list, optional
			A list of paths to result files.

		mode_numbers : list, optional
			A list with the modes we want to predict, e.g. [7, 8]. If left blank, all the modes of each result file will be given a prediction.

		Returns
		-------
		tuple
			Returns a namedtuple object with the following fields: predictions, variances and prediction_sids. Only predictions will be provided since ModeClassifiers are Keyvalue (1d) Predictors.

		"""

